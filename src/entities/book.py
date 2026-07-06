"""
entities/book.py

A simple class (Class & Object) representing a book in the
library's catalog. Demonstrates basic encapsulation.
"""


class Book:

    def __init__(self, isbn: str, title: str, author: str, total_copies: int):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._total_copies = total_copies
        self._available_copies = total_copies  # starts fully available

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def available_copies(self) -> int:
        return self._available_copies

    def is_available(self) -> bool:
        return self._available_copies > 0

    def issue_copy(self):
        """Reduce available copies by 1 when a book is issued."""
        if self._available_copies > 0:
            self._available_copies -= 1

    def return_copy(self):
        """Increase available copies by 1 when a book is returned."""
        if self._available_copies < self._total_copies:
            self._available_copies += 1

    def __str__(self):
        return (f"Book[{self._isbn}] '{self._title}' by {self._author} "
                f"({self._available_copies}/{self._total_copies} available)")

    # Converts a Book object into a plain dict - useful for
    # saving to a JSON file (see utils/file_handler.py)
    def to_dict(self) -> dict:
        return {
            "isbn": self._isbn,
            "title": self._title,
            "author": self._author,
            "total_copies": self._total_copies,
            "available_copies": self._available_copies,
        }