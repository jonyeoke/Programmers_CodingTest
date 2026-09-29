select concat('/home/grep/src/',b.board_id,'/',f.file_id,f.file_name,f.file_ext) as file_path
from used_goods_board as b join used_goods_file as f on b.board_id = f.board_id
where b.views = (select max(views) from used_goods_board)
order by file_id desc;