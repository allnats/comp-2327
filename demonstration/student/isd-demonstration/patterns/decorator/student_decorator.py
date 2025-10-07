__author__ = "Allendale Nato"
__version__ = "1.0.0"

from patterns.decorator.student_decoratable import StudentDecoratable

class StudentDecorator(StudentDecoratable):
    """Student Decorator.

    Implement the abstract superclass method.
    """

    def __init__(self, student: StudentDecoratable) -> None:
        self.__student = student

    @property
    def grade_point_average(self) -> float:
        return self.grade_point_average
