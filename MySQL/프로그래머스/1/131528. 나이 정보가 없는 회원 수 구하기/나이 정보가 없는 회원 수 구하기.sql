select count(user_id) as users
from user_info
where user_id in (select user_id
                 from user_info
                 where age is null)