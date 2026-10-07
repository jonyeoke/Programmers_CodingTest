select p.id, count(c.id) as child_count
from ecoli_data as c right outer join ecoli_data as p on c.parent_id = p.id
group by p.id
order by p.id asc;