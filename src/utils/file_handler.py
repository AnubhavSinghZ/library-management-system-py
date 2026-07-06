"""
utils/file_handler.py

UTILITY MODULE demonstrating FILE HANDLING.
Saves the book catalog to a JSON file and can load it back.
"""

import json
import os


def save_books_to_file(books: list, filepath: str):
    """books: list of Book objects (must have .to_dict())"""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        data = [book.to_dict() for book in books]
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        print(f"\nLibrary catalog saved to {filepath}")
    except (IOError, OSError) as e:
        print(f"Error writing to file: {e}")


def load_books_from_file(filepath: str) -> list:
    """Returns a list of plain dicts (raw data) read from the JSON file."""
    if not os.path.exists(filepath):
        print(f"No existing data file found at {filepath}")
        return []
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading file: {e}")
        return []