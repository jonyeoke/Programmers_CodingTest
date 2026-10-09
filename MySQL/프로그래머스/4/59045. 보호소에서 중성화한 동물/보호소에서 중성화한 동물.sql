select animal_id, animal_type, name
from animal_outs 
where animal_id in (select animal_id
                   from animal_ins
                   where SEX_UPON_INTAKE like 'Intact%')
and (SEX_UPON_OUTCOME like 'Spayed%' or SEX_UPON_OUTCOME like 'Neutered%')
order by animal_id