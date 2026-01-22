-- 코드를 작성해주세요
select e.id, e.genotype, p.genotype as PARENT_GENOTYPE 
from ecoli_data as e join ecoli_data as p on e.parent_id = p.id
WHERE 
    (e.genotype & p.genotype) = p.genotype
order by e.id asc;