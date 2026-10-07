with recursive timer as (
    select 0 as hour
    
    union all
    
    select hour+1
    from timer
    where hour<23
)

select t.hour, count(animal_id)
from timer t left outer join animal_outs o on t.hour = hour(o.datetime)
group by t.hour
order by t.hour asc;