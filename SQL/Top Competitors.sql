SELECT Hackers.hacker_id,Hackers.name
FROM Submissions

JOIN Challenges
ON Submissions.challenge_id = Challenges.challenge_id
JOIN Difficulty
ON Challenges.difficulty_level = Difficulty.difficulty_level
JOIN Hackers
ON Submissions.hacker_id = Hackers.hacker_id

WHERE Submissions.score = Difficulty.score and Challenges.difficulty_level=Difficulty.difficulty_level
GROUP BY Hackers.hacker_id, Hackers.name
HAVING COUNT(Submissions.hacker_id) > 1
ORDER BY COUNT(Submissions.hacker_id) desc,Hackers.hacker_id