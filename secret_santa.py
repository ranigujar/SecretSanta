import random
from csv_handler import CSVHandler
from employee import Employee

class SecretSanta:
    def __init__(self, employees, previous_assignments):
        self.employees = employees
        self.previous_assignments = previous_assignments
        self.assignments = {}

    def assign(self):
        """Assigns each employee a unique secret child."""
        available_recipients = self.employees[:]
        random.shuffle(available_recipients)

        for giver in self.employees:
            possible_recipients = [
                r for r in available_recipients
                if r.email != giver.email and r.email != self.previous_assignments.get(giver.email, None)
            ]

            if not possible_recipients:
                print("Error: Could not generate a valid assignment. Retrying...")
                return False  # Failed assignment, will retry

            recipient = random.choice(possible_recipients)
            self.assignments[giver] = recipient
            available_recipients.remove(recipient)

        return True  # Successfully assigned all

    def generate_assignments(self):
        """Tries multiple times to ensure valid assignment."""
        for _ in range(10):  # Try 10 times if needed
            if self.assign():
                return self.assignments
        raise Exception("Failed to generate valid assignments after multiple attempts.")
