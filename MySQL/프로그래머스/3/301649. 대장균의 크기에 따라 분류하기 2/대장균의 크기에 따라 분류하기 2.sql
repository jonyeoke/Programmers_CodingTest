select id,
    case
    when PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) * 100 <=25 then 'CRITICAL'
    when PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) * 100 <=50 then 'HIGH'
    when PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) * 100 <=75 then 'MEDIUM'
    else 'LOW'
    end as colony_name
from ecoli_data
order by id asc;