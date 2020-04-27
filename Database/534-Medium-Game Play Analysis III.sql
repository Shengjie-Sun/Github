/* Write your T-SQL query statement below */
SELECT player_id,
       event_date,
       SUM(games_played) OVER(PARTITION BY player_id ORDER BY event_date) AS games_played_so_far
  FROM Activity
 ORDER BY player_id, event_date

 # Write your MySQL query statement below
SELECT A1.player_id, A1.event_date, SUM(A2.games_played) AS games_played_so_far
  FROM Activity AS A1
       INNER JOIN Activity AS A2
       ON A1.player_id = A2.player_id
       AND A1.event_date >= A2.event_date
 GROUP BY A1.player_id, A1.event_date
 ORDER BY A1.player_id, A1.event_date