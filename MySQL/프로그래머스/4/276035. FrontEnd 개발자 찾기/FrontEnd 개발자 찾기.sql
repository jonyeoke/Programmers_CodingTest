select distinct d.id, d.email, d.first_name, d.last_name
from skillcodes s join developers d on (D.SKILL_CODE & S.CODE) > 0 
where s.category = 'Front End'
order by id asc;