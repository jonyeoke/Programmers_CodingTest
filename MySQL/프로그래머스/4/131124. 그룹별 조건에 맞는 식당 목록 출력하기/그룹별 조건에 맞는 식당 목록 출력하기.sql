select p.member_name, r.review_text, r.review_date
from member_profile p join rest_review r on p.member_id = r.member_id 
where p.member_id = (select p.member_id
                  from member_profile p join rest_review r on p.member_id = r.member_id
                  group by p.member_id
                  order by count(p.member_id) desc
                  limit 1)
order by r.review_date asc, r.review_text asc;