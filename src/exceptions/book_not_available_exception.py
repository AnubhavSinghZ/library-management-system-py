"""
exceptions/book_not_available_exception.py

CUSTOM EXCEPTION
Raised when a member tries to issue a book that has zero
available copies left.
"""


class BookNotAvailableException(Exception):
    def __init__(self, message: str):
        super().__init__(message)