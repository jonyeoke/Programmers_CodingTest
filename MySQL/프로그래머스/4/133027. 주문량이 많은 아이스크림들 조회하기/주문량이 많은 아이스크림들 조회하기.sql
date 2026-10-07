with total_orders as(
    select h.flavor, sum(h.total_order) + sum(j.total_order) as total_orderss
from first_half as h join july as j on h.flavor = j.flavor
group by h.flavor
)

select h.flavor
from first_half as h join july as j on h.shipment_id = j.shipment_id join total_orders s on h.flavor = s.flavor
group by h.flavor
order by s.total_orderss desc
limit 3