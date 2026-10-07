with bonus as(
select e.emp_no, avg(g.score) as avg_score
from hr_employees e join hr_grade g on e.emp_no = g.emp_no
group by e.emp_no)

select e.emp_no, e.emp_name,
case
when b.avg_score >= 96 then 'S'
when b.avg_score >= 90 then 'A'
when b.avg_score >= 80 then 'B'
else 'C'
end as grade,
case
when b.avg_score >= 96 then e.sal*0.2
when b.avg_score >= 90 then e.sal*0.15
when b.avg_score >= 80 then e.sal*0.1
else 0
end as bonus 
from hr_employees e join bonus b on e.emp_no = b.emp_no
