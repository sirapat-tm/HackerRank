SELECT if(grade<8,NULL,name) ,grade,marks
FROM students
JOIN grades
WHERE marks between min_mark and max_mark

ORDER BY grade desc,name