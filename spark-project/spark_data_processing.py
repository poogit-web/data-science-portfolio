from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

# Create Spark session
spark = SparkSession.builder \
    .appName("Employee Data Analysis") \
    .getOrCreate()

# Sample employee dataset
data = [
    ("Alice", "QA", 45000),
    ("Bob", "Data", 60000),
    ("Charlie", "QA", 47000),
    ("David", "DevOps", 55000),
    ("Eva", "Data", 62000)
]

columns = ["Employee", "Department", "Salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Display data
print("Employee Dataset:")
df.show()

# Group by department and calculate average salary
department_summary = df.groupBy("Department") \
    .agg(
        avg("Salary").alias("Average_Salary"),
        count("Employee").alias("Employee_Count")
    )

print("Department Summary:")
department_summary.show()

# Filter employees with salary above 50000
high_salary_df = df.filter(df.Salary > 50000)

print("Employees with Salary > 50000:")
high_salary_df.show()

# Stop Spark session
spark.stop()
