SET NOCOUNT ON;

WITH AlgoVolumes AS (
    SELECT 
        c.algorithm,
        DATEPART(QUARTER, dt) AS Quarter,
        SUM(volume) AS volume
    FROM 
        transactions t
    INNER JOIN 
        coins c ON t.coin_code = c.code 
    WHERE 
        dt >= '2020-01-01' AND dt < '2021-01-01'
    GROUP BY 
        c.algorithm, DATEPART(QUARTER, dt)
)

SELECT 
    a.algorithm,
    COALESCE(SUM(CASE WHEN av.Quarter = 1 THEN av.volume END), 0) AS transactions_Q1,
    COALESCE(SUM(CASE WHEN av.Quarter = 2 THEN av.volume END), 0) AS transactions_Q2,
    COALESCE(SUM(CASE WHEN av.Quarter = 3 THEN av.volume END), 0) AS transactions_Q3,
    COALESCE(SUM(CASE WHEN av.Quarter = 4 THEN av.volume END), 0) AS transactions_Q4
FROM 
    (SELECT DISTINCT algorithm FROM coins) a
LEFT JOIN 
    AlgoVolumes av ON a.algorithm = av.algorithm
GROUP BY 
    a.algorithm
ORDER BY 
    a.algorithm ASC;

