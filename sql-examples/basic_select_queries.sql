-- Basic SELECT Queries

SELECT * FROM employees;

SELECT employee_name, department
FROM employees;

SELECT employee_name, salary
FROM employees
WHERE salary > 50000;

SELECT *
FROM employees
ORDER BY salary DESC;
