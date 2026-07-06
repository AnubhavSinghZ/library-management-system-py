"""
interfaces/finable.py

INTERFACE (Abstraction)
Any class that "can calculate fines" implements this.
"""

from abc import ABC, abstractmethod


class Finable(ABC):

    @abstractmethod
    def calculate_fine(self, days_late: int) -> float:
        pass
    