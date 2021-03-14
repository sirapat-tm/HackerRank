SELECT concat(name,'(',upper(left(occupation,1)),')')
FROM occupations
ORDER BY name;

SELECT concat('There are a total of',' ',count(occupation),' ',lower(occupation),'s.')
FROM occupations
GROUP BY occupation
ORDER BY count(occupation),occupation;