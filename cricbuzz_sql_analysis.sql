CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    match TEXT,
    team1 TEXT,
    team2 TEXT
);

SELECT * FROM matches;

SELECT COUNT(*) FROM matches;

SELECT DISTINCT team1 FROM matches;

SELECT DISTINCT team2 FROM matches;

SELECT team1, COUNT(*) 
FROM matches
GROUP BY team1;


--QUERY 1 — Portugal matches
SELECT * 
FROM matches
WHERE team1 = 'Portugal' OR team2 = 'Portugal';

--QUERY 2 — Rajasthan Royals
SELECT * 
FROM matches
WHERE team1 = 'Rajasthan Royals' OR team2 = 'Rajasthan Royals';

--QUERY 3 — Brazil Women
SELECT * 
FROM matches
WHERE team1 = 'Brazil Women' OR team2 = 'Brazil Women';

--QUERY 4 — Indonesia
SELECT * 
FROM matches
WHERE team1 = 'Indonesia' OR team2 = 'Indonesia';

--SORTING DATA (ORDER BY)
--QUERY 1 — SORT BY TEAM NAME
SELECT * 
FROM matches
ORDER BY team1;

--QUERY 2 — DESCENDING ORDER
SELECT * 
FROM matches
ORDER BY team1 DESC;

--QUERY 3 — MOST MATCHES BY TEAM
SELECT team1, COUNT(*) 
FROM matches
GROUP BY team1
ORDER BY COUNT(*) DESC;

--QUERY 4 — LEAST MATCHES
SELECT team1, COUNT(*) 
FROM matches
GROUP BY team1
ORDER BY COUNT(*) ASC;

--QUERY 5 — SORT USING TEAM2
SELECT * 
FROM matches
ORDER BY team2;

--COMBINING WHERE + GROUP BY
--QUERY 1 — MATCHES OF A TEAM (COUNT)
SELECT team1, COUNT(*) 
FROM matches
WHERE team1 = 'Portugal'
GROUP BY team1;

--QUERY 2 — TOTAL MATCHES OF TEAM (BOTH SIDES)
SELECT COUNT(*) 
FROM matches
WHERE team1 = 'Portugal' OR team2 = 'Portugal';

--QUERY 3 — TOP TEAMS (FREQUENCY)
SELECT team1, COUNT(*) 
FROM matches
GROUP BY team1
ORDER BY COUNT(*) DESC;

--QUERY 4 — MATCHES WITH “WOMEN”
SELECT * 
FROM matches
WHERE match LIKE '%Women%';

--QUERY 5 — COUNT WOMEN MATCHES
SELECT COUNT(*) 
FROM matches
WHERE match LIKE '%Women%';

--QUERY 6 — MATCHES OF MULTIPLE TEAMS
SELECT * 
FROM matches
WHERE team1 IN ('Portugal', 'Brazil Women');

--FINAL INSIGHTS
--INSIGHT 1 — MOST ACTIVE TEAMS
SELECT team1, COUNT(*) 
FROM matches
GROUP BY team1
ORDER BY COUNT(*) DESC;

--INSIGHT 2 — TOTAL NUMBER OF MATCHES
SELECT COUNT(*) FROM matches;

--INSIGHT 3 — WOMEN MATCHES ANALYSIS
SELECT COUNT(*) 
FROM matches
WHERE match LIKE '%Women%';

--INSIGHT 4 — INTERNATIONAL MATCHES
SELECT * 
FROM matches
WHERE match NOT LIKE '%Women%';

--INSIGHT 5 — TEAM PARTICIPATION
SELECT COUNT(*) 
FROM matches
WHERE team1 = 'Portugal' OR team2 = 'Portugal';

--INSIGHT 6 — VARIETY OF TEAMS
SELECT DISTINCT team1 FROM matches;

SELECT 1;
