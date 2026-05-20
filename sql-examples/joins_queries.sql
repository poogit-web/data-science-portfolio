-- JOIN Queries

SELECT e.employee_name,
       d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;

SELECT e.employee_name,
       p.project_name
FROM employees e
LEFT JOIN projects p
ON e.employee_id = p.employee_id;

SELECT department_name,
       COUNT(employee_id) AS total_employees
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY department_name;
