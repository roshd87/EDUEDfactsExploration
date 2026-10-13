{#- Spec-conformance tests over edfacts_counts / edfacts_file output. -#}

{#- Each category code is a permitted value, and each value fits its layout length. -#}
{% test edfacts_conforms(model, fs, org_level) %}
  {%- set meta = edu_ext_edfacts.edfacts__sets(fs, org_level) -%}
  {%- set layout = edu_ext_edfacts.edfacts__seed_rows('edfacts_layouts', fs, org_level, "and record_type = 'data'", 'seq') -%}
  {%- set file = edu_ext_edfacts.edfacts__file(fs, org_level) -%}
  {%- set present = edu_ext_edfacts.edfacts__org_columns(org_level) + meta.cats + ['total_indicator', file['count_column'] if file else ''] -%}
  {%- set permitted = ref('edfacts_permitted_values') -%}
  {%- if not execute -%}select 1 where false{%- else -%}
  {%- for e in layout if e['column_name'] in present %}
select '{{ e['column_name'] }}' as column_name, cast({{ e['column_name'] }} as varchar) as bad_value, 'too long' as problem
from {{ model }} where length(cast({{ e['column_name'] }} as varchar)) > {{ e['length'] | int }}
union all
  {%- endfor %}
  {%- for c in meta.cats %}
select '{{ c }}', {{ c }}, 'not permitted'
from {{ model }} where {{ c }} is not null and {{ c }} not in (
    select code from {{ permitted }} where file_spec_id = '{{ fs }}' and column_name = '{{ c }}')
{{ 'union all' if not loop.last }}
  {%- endfor %}
  {%- endif -%}
{% endtest %}

{#- BRSI-style: every category set sums to the education unit total of its organization.
    Valid only where each set partitions the population (true for FS052). -#}
{% test edfacts_sets_sum_to_total(model, fs, org_level) %}
  {%- set org = edu_ext_edfacts.edfacts__org_columns(org_level) -%}
  {%- set file = edu_ext_edfacts.edfacts__file(fs, org_level) -%}
  {%- set count_column = file['count_column'] if file else 'n' -%}
with sums as (
    select {% for c in org %}{{ c }}, {% endfor %}category_set, sum({{ count_column }}) as set_total
    from {{ model }} group by {% for c in org %}{{ c }}, {% endfor %}category_set
),
totals as (
    select {% for c in org %}{{ c }}, {% endfor %}{{ count_column }} as unit_total
    from {{ model }} where category_set = 'Education Unit Total'
)
select sums.*, totals.unit_total
from sums join totals on 1 = 1{% for c in org %} and sums.{{ c }} = totals.{{ c }}{% endfor %}
where sums.set_total <> totals.unit_total
{% endtest %}

{#- Header and data records have exactly the spec's record length (CRLF excluded). -#}
{% test edfacts_record_lengths(model, fs, org_level) %}
  {%- set file = edu_ext_edfacts.edfacts__file(fs, org_level) -%}
select line_no, length(record) as record_length
from {{ model }}
where length(record) <> case when line_no = 0
    then {{ file['header_length'] | int if file else 0 }}
    else {{ file['data_length'] | int if file else 0 }} end
{% endtest %}
