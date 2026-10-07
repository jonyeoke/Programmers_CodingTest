with skills as(
select
    sum(case when category='Front End' then code end) as fe_code,
    sum(case when name='C#' then code end) as cs_code,
    sum(case when name='Python' then code end) as py_code
from skillcodes)

select
    case
        when (d.skill_code&s.fe_code) and (d.skill_code&s.py_code) then 'A'
        when d.skill_code & s.cs_code then 'B'
        when d.skill_code&s.fe_code then 'C'
    end as grade,
    id, email
from developers d, skills s
having grade is not null
order by grade asc, id asc;
