-- 코드를 입력하세요
select h.history_id, 
case
when p.duration_type is not null then c.daily_fee*(1-(p.discount_rate/100))*(datediff(h.end_date,h.start_date)+1)
else c.daily_fee*(datediff(h.end_date,h.start_date)+1)
end as fee
FROM CAR_RENTAL_COMPANY_CAR C JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON C.CAR_TYPE = P.CAR_TYPE
AND P.DURATION_TYPE = case
                        when datediff(h.end_date,h.start_date)+1 >=90 then '90일 이상'
                        when datediff(h.end_date,h.start_date)+1 >=30 then '30일 이상'
                        when datediff(h.end_date,h.start_date)+1 >=7 then '7일 이상'
                        else NULL
                    end
WHERE C.CAR_TYPE = '트럭'
group by h.history_id
order by fee desc, h.history_id desc;