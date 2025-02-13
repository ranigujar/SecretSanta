from csv_handler import CSVHandler
from secret_santa import SecretSanta

# File paths
employee_file = "data/employees.csv"
previous_assignments_file = "data/previous_assignments.csv"
output_file = "data/new_assignments.csv"

# Load data
employees = CSVHandler.read_employees(employee_file)
previous_assignments = CSVHandler.read_previous_assignments(previous_assignments_file)

if not employees:
    print("Error: No employees found.")
    exit(1)

# Run Secret Santa
santa = SecretSanta(employees, previous_assignments)
assignments = santa.generate_assignments()

# Save output
CSVHandler.write_assignments(output_file, assignments)
print(f"Secret Santa assignments saved to {output_file}")
