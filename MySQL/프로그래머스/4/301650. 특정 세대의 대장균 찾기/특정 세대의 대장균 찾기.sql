select g2.id
from ecoli_data p
join ecoli_data g1 on p.id = g1.parent_id
join ecoli_data g2 on g1.id = g2.parent_id
where p.parent_id IS NULL
order by g2.id asc;