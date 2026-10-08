select o.animal_id, o.animal_type, o.name
from animal_ins i join animal_outs o on i.animal_id = o.animal_id
where o.animal_id in (select animal_id
                     from animal_ins
                     where sex_upon_intake in ('Intact Female','Intact Male'))
and o.sex_upon_outcome in ('Spayed Female','Spayed Male','Neutered Male','Neutered Female')
order by o.animal_id asc;