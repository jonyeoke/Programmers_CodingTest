select
case
when month(DIFFERENTIATION_DATE) >= 1 and month(DIFFERENTIATION_DATE) <= 3 then '1Q'
when month(DIFFERENTIATION_DATE) >= 4 and month(DIFFERENTIATION_DATE) <= 6 then '2Q'
when month(DIFFERENTIATION_DATE) >= 7 and month(DIFFERENTIATION_DATE) <= 9 then '3Q'
else '4Q'
end as quarter, count(id) as ecoli_data
from ecoli_data
group by quarter
order by quarter asc;