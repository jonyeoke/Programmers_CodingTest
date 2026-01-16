SELECT es.ID,
case
when percent>0 and percent<=25 then 'CRITICAL'
when percent>25 and percent <=50 then 'HIGH'
when percent>50 and percent <=75 then 'MEDIUM'
else 'LOW'
end as colony_name
FROM (
    SELECT 
        id, 
        (RANK() OVER (ORDER BY size_of_colony DESC) / (SELECT COUNT(*) FROM ecoli_data) * 100) AS percent
    FROM ecoli_data
) AS es
ORDER BY es.id ASC;