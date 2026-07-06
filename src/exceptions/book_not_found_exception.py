"""
exceptions/book_not_found_exception.py

CUSTOM EXCEPTION
Raised when an ISBN is looked up but doesn't exist in the
library's catalog at all.
"""


class BookNotFoundException(Exception):
    def __init__(self, message: str):
        super().__init__(message)