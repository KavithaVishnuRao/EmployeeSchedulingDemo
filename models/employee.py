"""Represents an employee with scheduling-related attributes."""
class Employee:
    def __init__(self, employee_id, name, role, max_hours, availability):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.max_hours = max_hours
        self.availability = availability