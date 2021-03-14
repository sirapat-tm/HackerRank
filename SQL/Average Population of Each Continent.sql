SELECT country.continent,floor(avg(city.population))
FROM city
JOIN country
on city.countrycode = country.code
GROUP BY country.continent