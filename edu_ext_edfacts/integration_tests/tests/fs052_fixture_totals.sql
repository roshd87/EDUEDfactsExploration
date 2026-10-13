-- Education unit totals are distinct-student headcounts of the fixture (8 students, 2 LEAs, 3 schools).
select 'SEA' as level, student_count from {{ ref('fs052_sea_counts') }}
where category_set = 'Education Unit Total' and student_count <> 8
union all
select 'LEA', sum(student_count) from {{ ref('fs052_lea_counts') }}
where category_set = 'Education Unit Total' having sum(student_count) <> 8
union all
select 'School', count(*) from {{ ref('fs052_school_counts') }}
where category_set = 'Education Unit Total' having count(*) <> 3
