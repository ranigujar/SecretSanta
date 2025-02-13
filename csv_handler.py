import csv
from employee import Employee

class CSVHandler:
    @staticmethod
    def read_employees(file_path: str):
        """Reads employee data from a CSV file."""
        employees = []
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employees.append(Employee(row["Employee_Name"], row["Employee_EmailID"]))
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            return []
        return employees

    @staticmethod
    def read_previous_assignments(file_path: str):
        """Reads last year's assignments."""
        previous_assignments = {}
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    previous_assignments[row["Employee_EmailID"]] = row["Secret_Child_EmailID"]
        except FileNotFoundError:
            print(f"Warning: {file_path} not found. Assuming no previous assignments.")
        return previous_assignments

    @staticmethod
    def write_assignments(file_path: str, assignments):
        """Writes new Secret Santa assignments to a CSV file."""
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for giver, receiver in assignments.items():
                writer.writerow({
                    "Employee_Name": giver.name,
                    "Employee_EmailID": giver.email,
                    "Secret_Child_Name": receiver.name,
                    "Secret_Child_EmailID": receiver.email
                })
