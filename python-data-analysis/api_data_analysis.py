import pandas as pd

# Sample employee dataset
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["QA", "Data", "QA", "DevOps", "Data"],
    "Salary": [45000, 60000, 47000, 55000, 62000],
    "Experience": [2, 5, 3, 4, 6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Employee Dataset:")
print(df)

# Average salary
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

# Group by department
department_summary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(department_summary)

# Highest salary employee
highest_salary = df.loc[df["Salary"].idxmax()]

print("\nEmployee with Highest Salary:")
print(highest_salary)
