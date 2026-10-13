{#- EDFacts count and file macros, driven entirely by the spec seeds.

  Population contract: one row per counted unit (`unit_key`) per organization, with
  `lea_identifier_state` / `school_identifier_state` at the levels that need them and one column
  per category, named as the seed `column_name` and holding EDFacts permitted-value codes.
-#}

{% macro edfacts__seed_rows(seed, fs, org_level=none, where='', order_by='1') %}
  {%- set relation = ref(seed) -%}
  {%- if not execute -%}{{ return([]) }}{%- endif -%}
  {%- set sql -%}
    select * from {{ relation }}
    where file_spec_id = '{{ fs }}'
    {%- if org_level %} and org_level = '{{ org_level }}'{% endif %} {{ where }}
    order by {{ order_by }}
  {%- endset -%}
  {{ return(run_query(sql).rows) }}
{% endmacro %}

{% macro edfacts__org_columns(org_level) %}
  {{ return({'SEA': [], 'LEA': ['lea_identifier_state'],
             'School': ['lea_identifier_state', 'school_identifier_state']}[org_level]) }}
{% endmacro %}

{% macro edfacts__file(fs, org_level) %}
  {%- set rows = edu_ext_edfacts.edfacts__seed_rows('edfacts_files', fs, org_level) -%}
  {%- if execute and rows | length != 1 -%}
    {{ exceptions.raise_compiler_error(fs ~ ' ' ~ org_level ~ ': expected one edfacts_files row, got ' ~ rows | length) }}
  {%- endif -%}
  {{ return(rows[0] if rows else none) }}
{% endmacro %}

{#- {category_set: {order, ti, cols}} in set order, plus every category column in first-seen order. -#}
{% macro edfacts__sets(fs, org_level) %}
  {%- set sets, cats = {}, [] -%}
  {%- for r in edu_ext_edfacts.edfacts__seed_rows('edfacts_category_sets', fs, org_level, order_by='set_order, column_name') -%}
    {%- if r['category_set'] not in sets -%}
      {%- do sets.update({r['category_set']: {'order': r['set_order'] | int, 'ti': r['total_indicator'], 'cols': []}}) -%}
    {%- endif -%}
    {%- if r['column_name'] -%}
      {%- do sets[r['category_set']]['cols'].append(r['column_name']) -%}
      {%- if r['column_name'] not in cats -%}{%- do cats.append(r['column_name']) -%}{%- endif -%}
    {%- endif -%}
  {%- endfor -%}
  {{ return({'sets': sets, 'cats': cats}) }}
{% endmacro %}

{#- Count rows for every category set and total, zero-filled over permitted values.
    exclude_values: {column_name: [codes]} kept out of the zero-fill (e.g. grades the state
    does not use); a counted row with such a code still comes through. -#}
{% macro edfacts_counts(pop, fs, org_level, unit_key='k_student', exclude_values={}) %}
  {%- set org = edu_ext_edfacts.edfacts__org_columns(org_level) -%}
  {%- set meta = edu_ext_edfacts.edfacts__sets(fs, org_level) -%}
  {%- set file = edu_ext_edfacts.edfacts__file(fs, org_level) -%}
  {%- set permitted = ref('edfacts_permitted_values') -%}
  {%- if not execute -%}select 1 as _parse_only{%- else -%}
  {%- set cats, sets = meta.cats, meta.sets -%}
  {%- set keys = org + cats -%}
with counted as (
    select
        {% for c in keys %}{{ c }},
        {% endfor -%}
        {% for c in cats %}grouping({{ c }}) * {{ 2 ** loop.index0 }} + {% endfor %}0 as _mask,
        count(distinct {{ unit_key }}) as _n
    from {{ pop }}
    group by grouping sets (
        {%- for name, s in sets.items() %}
        ({{ (org + s.cols) | join(', ') }}){{ ',' if not loop.last }}
        {%- endfor %}
    )
),
labeled as (
    select {% for c in keys %}{{ c }}, {% endfor %}
    {%- for field in ['name', 'order', 'ti'] %}
        case _mask
        {%- for name, s in sets.items() -%}
          {%- set ns = namespace(mask=0) -%}
          {%- for c in cats %}{% if c not in s.cols %}{% set ns.mask = ns.mask + 2 ** loop.index0 %}{% endif %}{% endfor %}
            when {{ ns.mask }} then {{ s.order if field == 'order' else "'" ~ (name if field == 'name' else s.ti) ~ "'" }}
        {%- endfor %}
        end as {{ {'name': 'category_set', 'order': 'set_order', 'ti': 'total_indicator'}[field] }},
    {%- endfor %}
        _n
    from counted
),
orgs as (
    select distinct {{ org | join(', ') if org else '1 as _one' }} from {{ pop }}
),
zero_fill as (
    {%- for name, s in sets.items() %}
    select
        {% for c in org %}orgs.{{ c }}, {% endfor -%}
        {% for c in cats %}{{ 'v_' ~ c ~ '.code' if c in s.cols else 'cast(null as varchar)' }} as {{ c }}, {% endfor %}
        '{{ name }}' as category_set, {{ s.order }} as set_order, '{{ s.ti }}' as total_indicator, 0 as _n
    from orgs
    {%- for c in s.cols %}
    cross join (
        select code from {{ permitted }}
        where file_spec_id = '{{ fs }}' and column_name = '{{ c }}' and code <> 'MISSING'
        {%- for code in exclude_values.get(c, []) %} and code <> '{{ code }}'{% endfor %}
    ) as v_{{ c }}
    {%- endfor %}
    {{ 'union all' if not loop.last }}
    {%- endfor %}
)
select
    {% for c in keys %}{{ c }}, {% endfor %}category_set, set_order, total_indicator,
    cast(sum(_n) as bigint) as {{ file['count_column'] }}
from (
    select * from labeled
    union all
    select * from zero_fill
) as unioned
group by {% for c in keys %}{{ c }}, {% endfor %}category_set, set_order, total_indicator
  {%- endif -%}
{% endmacro %}

{#- Fixed-width record: every layout field left-justified and space-padded (HL-SHR-044).
    `values` maps a layout column_name to a SQL expression; unmapped fields read the column of
    the same name. Overlong values are truncated by rpad, so edfacts_conforms tests lengths. -#}
{% macro edfacts_record(fs, org_level, record_type, values={}) %}
  {%- set layout = edu_ext_edfacts.edfacts__seed_rows('edfacts_layouts', fs, org_level, "and record_type = '" ~ record_type ~ "'", 'seq') -%}
  {%- for e in layout if e['column_name'] != 'crlf' -%}
    rpad(coalesce(cast({{ values.get(e['column_name'], e['column_name']) }} as varchar), ''), {{ e['length'] | int }}, ' ')
    {{- ' || ' if not loop.last }}
  {%- endfor -%}
{% endmacro %}

{% macro edfacts_file_name(fs, org_level) %}
  {%- set file = edu_ext_edfacts.edfacts__file(fs, org_level) -%}
  {%- if not execute -%}{{ return('') }}{%- endif -%}
  {%- set name = var('edfacts_state_abbr') ~ file['level_abbr'] ~ file['file_name_token'] ~ var('edfacts_submission_id') ~ '.txt' -%}
  {%- if name | length > 25 -%}
    {{ exceptions.raise_compiler_error('EDFacts file name over 25 characters: ' ~ name) }}
  {%- endif -%}
  {{ return(name) }}
{% endmacro %}

{#- Whole file as (line_no, record): header at line 0, then numbered data records.
    Record order is unspecified by the spec; this one is set order, then organization, then codes. -#}
{% macro edfacts_file(counts, fs, org_level, file_identifier=none) %}
  {%- set org = edu_ext_edfacts.edfacts__org_columns(org_level) -%}
  {%- set meta = edu_ext_edfacts.edfacts__sets(fs, org_level) -%}
  {%- set file = edu_ext_edfacts.edfacts__file(fs, org_level) -%}
  {%- set file_name = edu_ext_edfacts.edfacts_file_name(fs, org_level) -%}
  {%- do ref('edfacts_layouts') -%}{#- edfacts_record reads it only at execute time -#}
  {%- if not execute -%}select 0 as line_no, '' as record{%- else -%}
  {%- set data_values = {
      'state_code': "'" ~ var('edfacts_state_code') ~ "'",
      'state_agency_number': "'" ~ var('edfacts_state_agency_number', '01') ~ "'",
      'table_name': "'" ~ file['table_name'] ~ "'",
      'explanation': "cast(null as varchar)"} -%}
  {%- for c in ['lea_identifier_state', 'school_identifier_state'] if c not in org -%}
    {%- do data_values.update({c: "''"}) -%}
  {%- endfor -%}
with numbered as (
    select *, row_number() over (
        order by set_order{% for c in org + meta.cats %}, {{ c }} nulls first{% endfor %}
    ) as file_record_number
    from {{ counts }}
)
select line_no, record from (
    select 0 as line_no, {{ edu_ext_edfacts.edfacts_record(fs, org_level, 'header', {
        'file_type': "'" ~ file['file_type'] ~ "'",
        'total_records_in_file': '(select count(*) from numbered)',
        'file_name': "'" ~ file_name ~ "'",
        'file_identifier': "'" ~ (file_identifier or file_name) ~ "'",
        'file_reporting_period': "'" ~ file['reporting_period'] ~ "'",
        'filler': "''"}) }} as record
    union all
    select file_record_number, {{ edu_ext_edfacts.edfacts_record(fs, org_level, 'data', data_values) }}
    from numbered
) as file_lines
order by line_no
  {%- endif -%}
{% endmacro %}
