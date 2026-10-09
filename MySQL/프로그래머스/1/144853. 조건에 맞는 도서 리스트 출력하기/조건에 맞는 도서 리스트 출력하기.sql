select book_id, published_date
from book
where year(published_date)='2021' and category='인문'
order by published_date asc;