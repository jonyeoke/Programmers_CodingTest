select c.item_id, c.item_name, c.rarity
from (item_info as p join item_tree as t on p.item_id = t.parent_item_id) join item_info as c on t.item_id = c.item_id
where p.rarity = 'RARE'
order by c.item_id desc;