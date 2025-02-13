from flask import Flask, request, jsonify
from secret_santa import SecretSanta
from csv_handler import CSVHandler
from models import Employee

app = Flask(__name__)

# CSV File Paths
EMPLOYEE_FILE = "data/employees.csv"
PREVIOUS_ASSIGNMENTS_FILE = "data/previous_year.csv"

@app.route("/generate", methods=["GET"])
def generate_secret_santa():
    """ Generate Secret Santa assignments and return them as JSON. """
    try:
        # Read employee data from CSV
        employees = CSVHandler.read_employees(EMPLOYEE_FILE)
        # Read previous year’s assignments
        previous_assignments = CSVHandler.read_previous_assignments(PREVIOUS_ASSIGNMENTS_FILE)

        # Generate new Secret Santa assignments
        santa = SecretSanta(employees, previous_assignments)
        assignments = santa.generate_assignments()

        # Format results as JSON response
        result = [
            {
                "Employee_Name": giver.name,
                "Employee_Email": giver.email,
                "Secret_Child_Name": receiver.name,
                "Secret_Child_Email": receiver.email,
            }
            for giver, receiver in assignments.items()
        ]
        
        return jsonify(result)  # Return JSON response

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle errors

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
