SELECT 
    e.emp_no AS EMP_NO,
    e.emp_name AS EMP_NAME,
    CASE 
        WHEN AVG(g.score) >= 96 THEN 'S'
        WHEN AVG(g.score) >= 90 THEN 'A'
        WHEN AVG(g.score) >= 80 THEN 'B'
        ELSE 'C'
    END AS GRADE,
    CASE 
        WHEN AVG(g.score) >= 96 THEN e.sal * 0.2
        WHEN AVG(g.score) >= 90 THEN e.sal * 0.15
        WHEN AVG(g.score) >= 80 THEN e.sal * 0.1
        ELSE 0
    END AS BONUS
FROM HR_EMPLOYEES e
JOIN HR_GRADE g ON e.emp_no = g.emp_no
WHERE g.year = 2022
GROUP BY e.emp_no, e.emp_name, e.sal
ORDER BY e.emp_no;