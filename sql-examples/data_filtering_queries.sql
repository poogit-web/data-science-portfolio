-- Data Filtering Queries

SELECT *
FROM employees
WHERE department = 'Data';

SELECT *
FROM employees
WHERE salary BETWEEN 40000 AND 60000;

SELECT *
FROM employees
WHERE employee_name LIKE 'A%';

SELECT *
FROM employees
WHERE experience_years >= 5;
