select h.history_id, 
case
when p.duration_type is not null then c.daily_fee*(1-(p.discount_rate/100))*(datediff(h.end_date,h.start_date)+1)
else c.daily_fee*(datediff(h.end_date,h.start_date)+1)
end as fee
from CAR_RENTAL_COMPANY_CAR c join CAR_RENTAL_COMPANY_RENTAL_HISTORY h on c.car_id = h.car_id
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p on p.car_type=c.car_type
and p.duration_type = case
                        when datediff(h.end_date,h.start_date)+1 >=90 then '90일 이상'
                        when datediff(h.end_date,h.start_date)+1 >=30 then '30일 이상'
                        when datediff(h.end_date,h.start_date)+1 >=7 then '7일 이상'
                        else NULL
                    end
where c.car_type = '트럭'
group by h.history_id
order by fee desc, h.history_id desc;