WITH RECURSIVE depth AS (
    SELECT id, parent_id, 1 AS gen
    FROM ecoli_data
    WHERE parent_id IS NULL
    
    UNION ALL

    SELECT c.id, c.parent_id, p.gen + 1
    FROM ecoli_data c
    JOIN depth p ON c.parent_id = p.id 
)
SELECT 
    COUNT(id) AS COUNT, 
    gen AS GENERATION
FROM depth
WHERE id NOT IN (
    SELECT DISTINCT parent_id 
    FROM ecoli_data 
    WHERE parent_id IS NOT NULL
)
GROUP BY gen
ORDER BY GENERATION ASC;