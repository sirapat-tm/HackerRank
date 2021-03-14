SELECT city,length(City)
FROM Station
ORDER BY length(City),city DESC
LIMIT 1;

SELECT city,length(City)
FROM Station
ORDER BY length(City) ASC
LIMIT 1;