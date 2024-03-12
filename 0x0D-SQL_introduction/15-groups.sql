-- lists the number of records with the same score in the table second_table
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY SCORE ORDER BY number DESC;
