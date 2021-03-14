SELECT city.name
FROM city
JOIN country
on city.countrycode = country.code
WHERE country.continent = 'Africa'