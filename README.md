# 📚 Library Management System — Python OOP Project

A beginner-friendly, package-structured Python console application that models a small **Library Management System** (books, members, librarians, issuing/returning, fines, and file storage).

Built specifically to demonstrate core **Object-Oriented Programming (OOP)** concepts organized like a real-world Python project.

---

## 📂 Project Structure

```
📁 library-management-system/
│
├── 📁 src/                          → All source code lives here
│   │
│   ├── 📁 entities/                 → Core objects (the "things" in the system)
│   │   ├── person.py                → Abstract base class (Member & Librarian inherit from this)
│   │   ├── member.py                → Represents a library member (inheritance + constructors)
│   │   ├── librarian.py             → Represents a librarian (inheritance)
│   │   └── book.py                  → Represents a book in the catalog
│   │
│   ├── 📁 interfaces/               → Contracts that classes must follow
│   │   ├── reservable.py            → For anything that can reserve a book
│   │   └── finable.py               → For anything that can calculate fines
│   │
│   ├── 📁 services/                 → Business logic / core operations
│   │   ├── library_service.py       → Handles catalog, members, issue/return
│   │   └── fine_service.py          → Calculates fines (implements Finable)
│   │
│   ├── 📁 exceptions/               → Custom error handling
│   │   ├── book_not_available_exception.py
│   │   ├── book_not_found_exception.py
│   │   └── member_limit_exceeded_exception.py
│   │
│   ├── 📁 utils/                    → Helper/utility modules
│   │   └── file_handler.py          → Saves/loads catalog data as JSON
│   │
│   └── main.py                      → Entry point — runs the whole demo
│
├── 📁 data/                         → Generated JSON data (created on first run)
├── README.md                        → Project documentation
├── requirements.txt                 → Python dependencies (none needed - stdlib only)
├── .gitignore                       → Files Git should ignore
└── LICENSE                          → MIT License
```

---

## 🚀 How to Run

**Requirements:** Python 3.8+

```bash
# 1. Clone the repository
git clone https://github.com/AnubhavSinghZ/library-management-system-py.git
cd library-management-system/src

# 2. Run it
python main.py
```

Running the program will:
1. Create Member, Librarian, and Book objects
2. Register members and add books to the catalog
3. Demonstrate a member reserving a book (`Reservable` interface)
4. Issue books to members, including a deliberate failure (no copies left)
5. Push a member past their borrowing limit to trigger a custom exception
6. Calculate late fines using default and custom rates
7. Return a book
8. Save the full catalog to `data/library_data.json`

---

## 🧠 OOP Concepts Covered

| # | Concept | File |
|---|---------|------|
| 1 | Class & Object | `book.py`, `member.py`, `librarian.py`, `main.py` |
| 2 | Constructors (`__init__`) | `person.py`, `member.py`, `librarian.py`, `book.py` |
| 3 | Encapsulation (`_private` attrs + `@property`) | `person.py`, `book.py` |
| 4 | Inheritance | `Member(Person)`, `Librarian(Person)` |
| 5 | Runtime Polymorphism (Overriding) | `get_role()`, `__str__()` in each subclass |
| 6 | Method Overloading (Python-style, via default args) | `FineService.calculate_fine()` |
| 7 | Abstraction (Abstract Base Class - `abc.ABC`) | `person.py` |
| 8 | Abstraction (Interfaces via ABC) | `reservable.py`, `finable.py` |
| 9 | Interface Implementation | `Member(Reservable)`, `FineService(Finable)` |
| 10 | Custom Exception Handling | all files in `exceptions/` |
| 11 | Static / Class Members | `Member._counter`, `Member.MAX_BOOKS_ALLOWED` |
| 12 | Collections (dict, list) | `library_service.py` |
| 13 | File Handling (JSON) | `file_handler.py` |
| 14 | Packages & Modules | `entities`, `interfaces`, `services`, `exceptions`, `utils` |

> **Note on Method Overloading:** Python doesn't support true method overloading (multiple methods with the same name but different signatures) the way Java does. Instead, Python achieves the same flexibility using **default arguments** and `*args`/`**kwargs`. `FineService.calculate_fine()` demonstrates this Pythonic equivalent.

---

## 🖥️ Sample Output

```
==================================================
 LIBRARY MANAGEMENT SYSTEM (OOP DEMO)
==================================================

--- Demonstrating Runtime Polymorphism ---
Name: Aditi, Age: 19, Role: Member, ID: 1, Borrowed: 0/3
Name: Rohan, Age: 20, Role: Member, ID: 2, Borrowed: 0/3
Name: Mr. Verma, Age: 40, Role: Librarian, Employee ID: EMP101, Dept: Central Library
...
--- Testing Borrow Limit ---
Issued 'Head First Design Patterns' to Aditi
Issued 'Clean Code' to Aditi
Caught custom exception -> Aditi has already borrowed the maximum allowed (3) books.
...
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Concepts:** Core OOP, Abstract Base Classes, Custom Exceptions, Collections, File I/O (JSON), Packages
- **Dependencies:** None (Python standard library only)

---

## 📖 Why This Project?

Built as part of my **AKTU B.Tech 2nd Year** coursework to practically apply and revise Object-Oriented Programming concepts in Python using a proper multi-module project layout, instead of just learning them theoretically.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋 Author

**Your Name**
- GitHub: [@AnubhavSinghZ](https://github.com/AnubhavSinghZ)
- LinkedIn: [Anubhav Kumar Singh]

⭐ If you found this helpful, consider giving the repo a star!
