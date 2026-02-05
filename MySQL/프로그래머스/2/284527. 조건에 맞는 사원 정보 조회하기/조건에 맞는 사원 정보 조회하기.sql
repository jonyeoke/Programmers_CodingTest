select sum(score) as score, e.emp_no, e.emp_name, e.position, e.email
from hr_grade as g join hr_employees as e on g.emp_no = e.emp_no
where g.year = 2022
group by emp_no
order by score desc
limit 1

