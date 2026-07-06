"""
entities/librarian.py

INHERITANCE: Librarian extends Person
(You could extend this further, e.g. "SeniorLibrarian extends
Librarian", to demonstrate multilevel inheritance.)
"""

from entities.person import Person


class Librarian(Person):

    def __init__(self, name: str, age: int, employee_id: str, department: str):
        super().__init__(name, age)
        self._employee_id = employee_id
        self._department = department

    @property
    def employee_id(self) -> str:
        return self._employee_id

    @property
    def department(self) -> str:
        return self._department

    # RUNTIME POLYMORPHISM (Method Overriding)
    def get_role(self) -> str:
        return "Librarian"

    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self._employee_id}, Dept: {self._department}"