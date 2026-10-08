select year(o.sales_date) as year,month(o.sales_date) as month, count(distinct o.user_id) as purchased_users
,round(count(distinct o.user_id)/(
    select count(*)
    from user_info
    where date_format(joined, '%Y') = '2021'
),1) as purchased_ratio
from user_info i join online_sale o on i.user_id = o.user_id
where date_format(i.joined, '%Y')='2021'
group by year(o.sales_date),month(o.sales_date)
order by year asc, month asc;