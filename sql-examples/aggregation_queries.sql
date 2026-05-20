-- Aggregation Queries

SELECT department,
       AVG(salary) AS average_salary
FROM employees
GROUP BY department;

SELECT department,
       MAX(salary) AS highest_salary
FROM employees
GROUP BY department;

SELECT department,
       COUNT(*) AS employee_count
FROM employees
GROUP BY department;

SELECT department,
       SUM(salary) AS total_salary
FROM employees
GROUP BY department;
