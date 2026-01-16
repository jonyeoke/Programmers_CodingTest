select count(*) as FISH_COUNT, MONTH(f.time) as MONTH
from fish_info as f
group by MONTH
order by MONTH(f.time) asc;