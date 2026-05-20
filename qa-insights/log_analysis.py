# Log Analysis Script

log_file = "sample_logs.txt"

error_count = 0
warning_count = 0
info_count = 0

errors = []
warnings = []

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:
    if "ERROR" in line:
        error_count += 1
        errors.append(line.strip())

    elif "WARNING" in line:
        warning_count += 1
        warnings.append(line.strip())

    elif "INFO" in line:
        info_count += 1

# Display summary
print("===== LOG ANALYSIS SUMMARY =====")

print(f"\nTotal INFO messages: {info_count}")
print(f"Total WARNING messages: {warning_count}")
print(f"Total ERROR messages: {error_count}")

print("\nWarnings Detected:")
for warning in warnings:
    print("-", warning)

print("\nErrors Detected:")
for error in errors:
    print("-", error)
