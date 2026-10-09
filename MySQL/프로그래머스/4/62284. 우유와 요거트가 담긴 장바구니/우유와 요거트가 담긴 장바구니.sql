select distinct c.cart_id
from cart_products c join (select *
                        from cart_products
                        where name='milk') m on c.cart_id = m.cart_id
                    join (select *
                        from cart_products
                        where name='yogurt') y on c.cart_id = y.cart_id
group by c.id
order by c.cart_id