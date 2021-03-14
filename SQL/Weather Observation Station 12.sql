SELECT DISTINCT city
FROM Station
WHERE city NOT REGEXP '^[aeiou]' OR city NOT REGEXP '[aeiou]$'