select distinct d.id, d.email, d.first_name, d.last_name
from skillcodes s join developers d on (s.code&d.skill_code)>0
where s.category='Front End'
order by d.id asc;