class Employee:
    def __init__(self, name: str, email: str):
        """Initialize an Employee with a name and email."""
        self.name = name
        self.email = email

    def __repr__(self):
        """Return a string representation of the Employee object."""
        return f"Employee(Name: {self.name}, Email: {self.email})"
