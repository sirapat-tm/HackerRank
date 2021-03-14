SELECT sum(city.population)
FROM city
JOIN country
on city.countrycode = country.code
WHERE country.continent = 'Asia'