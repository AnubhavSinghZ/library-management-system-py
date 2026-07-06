"""
interfaces/reservable.py

INTERFACE (Abstraction)
Python doesn't have a dedicated "interface" keyword like Java,
so we use an abstract class with only abstract methods to
achieve the same effect. Any class that "can reserve a book"
implements this.
"""

from abc import ABC, abstractmethod


class Reservable(ABC):

    @abstractmethod
    def reserve_book(self, isbn: str):
        pass