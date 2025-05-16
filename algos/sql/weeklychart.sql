SET NOCOUNT ON;


/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

WITH maxScoresPerParticipantPerEvent AS (
    SELECT event_id, participant_name, max(score) as score
    from scoretable
    group by event_id, participation_name    
),
scoresPerEvent AS (
    SELECT event_id, participant_name, score
    from maxScoresPerParticipantPerEvent
    order by event_id asc, score  desc, participant_name asc
)

SELECT 
    event_id, STRING_AGG(name, ', ') AS concatenated_names
FROM 
    scoresPerEvent
WHERE 
    some_condition;  -- Replace with your actual condition




    

SELECT 
  event_id, 
  GROUP_CONCAT(IF(ranking = 1, participant_name, NULL) ORDER BY participant_name ASC SEPARATOR ',') AS first,
  GROUP_CONCAT(IF(ranking = 2, participant_name, NULL) ORDER BY participant_name ASC SEPARATOR ',') AS second,
  GROUP_CONCAT(IF(ranking = 3, participant_name, NULL) ORDER BY participant_name ASC SEPARATOR ',') AS third
FROM (
  SELECT 
    event_id, 
    participant_name, 
    MAX(score) AS best_score,
    DENSE_RANK() OVER (PARTITION BY event_id ORDER BY MAX(score) DESC) AS ranking
  FROM scoretable
  GROUP BY event_id, participant_name
) AS rankings
WHERE ranking <= 3
GROUP BY event_id
ORDER BY event_id ASC;