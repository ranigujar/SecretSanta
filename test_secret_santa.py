# import unittest
# from employee import Employee
# from secret_santa import SecretSanta

# class TestSecretSanta(unittest.TestCase):
#     def setUp(self):
#         self.employees = [
#             Employee("Alice", "alice@example.com"),
#             Employee("Bob", "bob@example.com"),
#             Employee("Charlie", "charlie@example.com"),
#             Employee("David", "david@example.com")
#         ]
#         self.previous_assignments = {
#             "alice@example.com": "bob@example.com",
#             "bob@example.com": "charlie@example.com",
#             "charlie@example.com": "david@example.com",
#             "david@example.com": "alice@example.com"
#         }

#     def test_no_self_assignment(self):
#         santa = SecretSanta(self.employees, self.previous_assignments)
#         assignments = santa.generate_assignments()
#         for giver, receiver in assignments.items():
#             self.assertNotEqual(giver.email, receiver.email)

#     def test_no_repeat_assignments(self):
#         santa = SecretSanta(self.employees, self.previous_assignments)
#         assignments = santa.generate_assignments()
#         for giver, receiver in assignments.items():
#             self.assertNotEqual(receiver.email, self.previous_assignments[giver.email])

# if __name__ == "__main__":
#     unittest.main()
