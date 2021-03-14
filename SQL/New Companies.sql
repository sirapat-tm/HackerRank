SELECT c.company_code,
	c.founder,
	count(distinct l.lead_manager_code),
	count(distinct s.senior_manager_code),
	count(distict m.manager_code),
	count(distinct e.employee_code)
FROM Company as c
JOIN Lead_manager as L 
	ON c.company_code=l.company_code
JOIN Senior_manager as s
	ON l.lead_manager_code = s.lead_manager_code
JOIN Manager as m
	ON s.senior_manager_code = m.senior_manager_code
JOIN Employee as e
	ON m.manager_code = e.manager_code
GROUP BY C.company_code, C.founder
ORDER BY c.company_code