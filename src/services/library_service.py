"""
services/library_service.py

SERVICE CLASS: manages the book catalog, member registry,
and the issue/return workflow.
Demonstrates COLLECTIONS: dict (for O(1) lookup by ISBN / ID)
and list (for iteration/ordering).
"""

from entities.book import Book
from entities.member import Member
from exceptions.book_not_available_exception import BookNotAvailableException
from exceptions.book_not_found_exception import BookNotFoundException
from exceptions.member_limit_exceeded_exception import MemberLimitExceededException


class LibraryService:

    def __init__(self):
        self._books = {}     # isbn (str) -> Book object
        self._members = {}   # member_id (int) -> Member object

    # ---------------- Book catalog management ----------------
    def add_book(self, book: Book):
        self._books[book.isbn] = book
        print(f"Added to catalog: {book}")

    def get_book(self, isbn: str) -> Book:
        book = self._books.get(isbn)
        if book is None:
            raise BookNotFoundException(f"No book found with ISBN {isbn}")
        return book

    def list_all_books(self):
        print("\n--- Library Catalog ---")
        for book in self._books.values():
            print(book)

    # ---------------- Member management ----------------
    def register_member(self, member: Member):
        self._members[member.member_id] = member
        print(f"Registered member: {member.name} (ID: {member.member_id})")

    def find_member(self, member_id: int) -> Member:
        return self._members.get(member_id)

    # ---------------- Issue / Return workflow ----------------
    def issue_book(self, member_id: int, isbn: str):
        member = self.find_member(member_id)
        book = self.get_book(isbn)  # raises BookNotFoundException if missing

        if not member.can_borrow_more():
            raise MemberLimitExceededException(
                f"{member.name} has already borrowed the maximum allowed "
                f"({Member.MAX_BOOKS_ALLOWED}) books."
            )

        if not book.is_available():
            raise BookNotAvailableException(
                f"'{book.title}' has no available copies right now."
            )

        book.issue_copy()
        member.borrow_book(isbn)
        print(f"Issued '{book.title}' to {member.name}")

    def return_book(self, member_id: int, isbn: str):
        member = self.find_member(member_id)
        book = self.get_book(isbn)

        book.return_copy()
        member.return_book(isbn)
        print(f"{member.name} returned '{book.title}'")

    def get_all_books(self) -> list:
        return list(self._books.values())