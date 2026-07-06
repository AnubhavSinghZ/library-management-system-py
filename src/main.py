"""
main.py

============================================================
 LIBRARY MANAGEMENT SYSTEM - Entry Point
 
============================================================
See README.md for the full concept-to-file mapping.

Run from inside the "src" folder:
    python main.py
============================================================
"""

from entities.book import Book
from entities.member import Member
from entities.librarian import Librarian
from services.library_service import LibraryService
from services.fine_service import FineService
from exceptions.book_not_available_exception import BookNotAvailableException
from exceptions.book_not_found_exception import BookNotFoundException
from exceptions.member_limit_exceeded_exception import MemberLimitExceededException
from utils.file_handler import save_books_to_file


def main():
    print("=" * 50)
    print(" LIBRARY MANAGEMENT SYSTEM (OOP DEMO)")
    print("=" * 50)

    # ---- Creating OBJECTS ----
    book1 = Book("978-0134685991", "Effective Java", "Joshua Bloch", 2)
    book2 = Book("978-1491910399", "Python Crash Course", "Eric Matthes", 1)
    book3 = Book("978-0596007126", "Head First Design Patterns", "Freeman & Robson", 1)
    book4 = Book("978-0132350884", "Clean Code", "Robert C. Martin", 1)
    book5 = Book("978-0201633610", "Design Patterns (GoF)", "Gamma et al.", 1)

    member1 = Member("Aditi", 19)
    member2 = Member("Rohan", 20)
    librarian1 = Librarian("Mr. Verma", 40, "EMP101", "Central Library")

    # ---- Runtime Polymorphism: same reference "type" (Person),
    # different actual objects, different get_role()/__str__ ----
    print("\n--- Demonstrating Runtime Polymorphism ---")
    for person in [member1, member2, librarian1]:
        print(person)

    # ---- LibraryService: dict-based catalog + member registry ----
    library = LibraryService()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    library.register_member(member1)
    library.register_member(member2)

    library.list_all_books()

    # ---- Reservable interface demo ----
    print("\n--- Reservation (Interface: Reservable) ---")
    member1.reserve_book(book3.isbn)

    # ---- Issue / Return workflow + exception handling ----
    print("\n--- Issuing Books ---")
    try:
        library.issue_book(member1.member_id, book1.isbn)
        library.issue_book(member2.member_id, book2.isbn)
        library.issue_book(member2.member_id, book2.isbn)  # this should fail - no copies left
    except BookNotAvailableException as e:
        print(f"Caught custom exception -> {e}")
    except BookNotFoundException as e:
        print(f"Caught custom exception -> {e}")

    # ---- Triggering MemberLimitExceededException ----
    # member1 already borrowed book1 above. Give them 2 more
    # (reaching MAX_BOOKS_ALLOWED = 3), then try a 4th to force
    # the limit exception specifically.
    print("\n--- Testing Borrow Limit ---")
    try:
        library.issue_book(member1.member_id, book3.isbn)  # 2nd book for member1
        library.issue_book(member1.member_id, book4.isbn)  # 3rd book for member1 -> hits limit
        library.issue_book(member1.member_id, book5.isbn)  # 4th book -> exceeds limit of 3
    except MemberLimitExceededException as e:
        print(f"Caught custom exception -> {e}")
    except (BookNotAvailableException, BookNotFoundException) as e:
        print(f"Caught custom exception -> {e}")
    finally:
        print("Borrow-limit check complete.")

    # ---- FineService: interface implementation + overload-style methods ----
    print("\n--- Fine Calculation (Interface: Finable) ---")
    fine_service = FineService()
    fine1 = fine_service.calculate_fine(4)             # uses default rate
    fine2 = fine_service.calculate_fine(4, 10.0)        # custom rate
    fine3 = fine_service.calculate_fine_for_multiple([2, 5, 0])  # multiple books
    print(f"Fine for 4 days late (default rate): Rs.{fine1}")
    print(f"Fine for 4 days late (custom rate):  Rs.{fine2}")
    print(f"Total fine for multiple books late:  Rs.{fine3}")

    # ---- Returning a book ----
    print("\n--- Returning a Book ---")
    library.return_book(member1.member_id, book1.isbn)

    # ---- File Handling demo ----
    save_books_to_file(library.get_all_books(), "../data/library_data.json")

    print("\n" + "=" * 50)
    print(" PROGRAM END")
    print("=" * 50)


if __name__ == "__main__":
    main()