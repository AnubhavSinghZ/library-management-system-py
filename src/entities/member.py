"""
entities/member.py

INHERITANCE: Member extends Person (single level)
Also implements Reservable interface -> a Member can reserve books.
"""

from entities.person import Person
from interfaces.reservable import Reservable


class Member(Person, Reservable):

    # STATIC / CLASS MEMBER: shared across ALL Member objects.
    # Used to auto-generate a unique member ID for every new member.
    _counter = 1
    MAX_BOOKS_ALLOWED = 3  # a "class constant"

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self._member_id = Member._counter
        Member._counter += 1
        self._borrowed_books = []       # list of ISBNs currently borrowed
        self._reserved_books = []       # list of ISBNs reserved

    @property
    def member_id(self) -> int:
        return self._member_id

    @property
    def borrowed_books(self) -> list:
        return self._borrowed_books

    def can_borrow_more(self) -> bool:
        return len(self._borrowed_books) < Member.MAX_BOOKS_ALLOWED

    def borrow_book(self, isbn: str):
        self._borrowed_books.append(isbn)

    def return_book(self, isbn: str):
        if isbn in self._borrowed_books:
            self._borrowed_books.remove(isbn)

    # RUNTIME POLYMORPHISM (Method Overriding)
    def get_role(self) -> str:
        return "Member"

    # Implementing Reservable interface's method
    def reserve_book(self, isbn: str):
        self._reserved_books.append(isbn)
        print(f"{self.name} reserved book with ISBN {isbn}")

    def __str__(self):
        return (f"{super().__str__()}, ID: {self._member_id}, "
                f"Borrowed: {len(self._borrowed_books)}/{Member.MAX_BOOKS_ALLOWED}")