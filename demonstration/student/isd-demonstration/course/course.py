__author__ = "Allendale Nato"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from department.department import Department
from student.student import Student

class Course(ABC):
    """Represents a course.

    Args:
        name (str): The name of the course.
        department (Department): The nam eof the department in which
            the course exist.
        credit_hours (int): The  number of credit hours.

    """

    def __init__(self, name: str,
                 department: Department,
                 credit_hours: int,
                 capacity: int,
                 current_enrollment: int) -> None:
        """Initialize the Course class."""
        if len(name.strip()) <= 0:
            raise ValueError("Name connot be blank.")

        if not isinstance(department, Department):
            raise ValueError("Department is invalid.")

        if not isinstance(credit_hours, int):
            raise ValueError("Credit hours must be numeric.")

        if not isinstance(capacity, int):
            raise ValueError("Capacity must be numeric.")

        if not isinstance(current_enrollment, int):
            raise ValueError("Capacity must be numeric.")


        # Name mangling _ClassName.__name
        # Private variables
        self.__name = name
        self.__department = department
        self.__credit_hours = credit_hours

        # Protected variables
        self._capacity = capacity
        self._current_enrollment = current_enrollment

    @property
    def name(self) -> str:
        return self.__name

    @property
    def department(self) -> Department:
        return self.__department

    @property
    def credit_hours(self) -> int:
        return self.__credit_hours

    def __str__(self) -> str:
        department_titlecase = self.__department.name.replace("_", " ").title()
        return (f"Course: {self.__name}\n"
                f"Department: {department_titlecase}\n"
                f"Credit Hours: {self.__credit_hours}")
