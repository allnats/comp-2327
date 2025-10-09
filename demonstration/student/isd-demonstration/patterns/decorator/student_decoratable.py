__author__ = "Allendale Nato"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class StudentDecoratable(ABC):
    """Represent an interface to be applied to the Student class."""

    @abstractmethod
    def grade_point_average(self) -> float:
        """Implement code to calculate grade point average."""
        pass
