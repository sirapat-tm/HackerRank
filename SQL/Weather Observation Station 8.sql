SELECT DISTINCT city
FROM Station
WHERE (city LIKE 'a%' 
    OR city LIKE 'e%' 
    OR city LIKE 'i%'
    OR city LIKE 'o%'
    OR city LIKE 'u%')
AND  (city LIKE '%a' 
    OR city LIKE '%e' 
    OR city LIKE '%i'
    OR city LIKE '%o'
    OR city LIKE '%u')

*/
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[aeiou].*[aeiou]$';
*/