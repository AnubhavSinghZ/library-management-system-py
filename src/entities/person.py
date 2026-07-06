"""
entities/person.py

ABSTRACT BASE CLASS (Abstraction)
Person is a blueprint - you can never do Person("name", 20).
Only concrete subclasses like Member and Librarian can be
instantiated. This mirrors the "abstract class" concept from
the AKTU OOP syllabus.
"""

from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name: str, age: int):
        # ENCAPSULATION: attributes prefixed with _ are "private by
        # convention" in Python. Access only via properties below.
        self._name = name
        self._age = age

    # --- Getters and Setters using @property (Encapsulation) ---
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if value > 0:  # basic validation
            self._age = value

    # Abstract method - every subclass MUST implement this.
    # This is where runtime polymorphism (overriding) comes in.
    @abstractmethod
    def get_role(self) -> str:
        pass

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}, Role: {self.get_role()}"