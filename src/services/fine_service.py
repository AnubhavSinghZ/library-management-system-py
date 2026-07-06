"""
services/fine_service.py

SERVICE CLASS implementing the Finable interface.
Also demonstrates Python's take on METHOD OVERLOADING.
(Python doesn't support true overloading like Java - instead
we use default arguments / *args to let one method handle
multiple "shapes" of input, which is the Pythonic equivalent.)
"""

from interfaces.finable import Finable


class FineService(Finable):

    DEFAULT_RATE_PER_DAY = 5.0  # Rs. 5 per day late, by default

    # Implementing the interface method
    def calculate_fine(self, days_late: int, rate_per_day: float = None) -> float:
        """
        Calculate fine for a late return.
        - calculate_fine(4)          -> uses default rate
        - calculate_fine(4, 10.0)    -> uses a custom rate
        This optional-argument style is how Python achieves the
        same flexibility Java gets from method overloading.
        """
        if days_late <= 0:
            return 0.0

        rate = rate_per_day if rate_per_day is not None else FineService.DEFAULT_RATE_PER_DAY
        return round(days_late * rate, 2)

    def calculate_fine_for_multiple(self, days_late_list: list, rate_per_day: float = None) -> float:
        """Another 'overload-style' method: total fine across several books."""
        return round(sum(self.calculate_fine(d, rate_per_day) for d in days_late_list), 2)