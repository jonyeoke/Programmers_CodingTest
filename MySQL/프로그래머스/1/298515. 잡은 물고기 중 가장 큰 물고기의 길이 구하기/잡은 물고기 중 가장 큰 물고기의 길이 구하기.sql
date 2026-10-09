select concat(length,'cm')
from fish_info
group by length
order by length desc
limit 1;