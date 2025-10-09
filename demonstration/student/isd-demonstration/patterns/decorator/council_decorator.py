__author__ = "Allendale Nato"
__version__ = "1.0.0"

from patterns.decorator.student_decorator import StudentDecorator

class CouncilDecorator(StudentDecorator):

    @property
    def grade_point_average(self) -> float:
        gpa = super().grade_point_average

        increases: dict[float, float] = {
            4.13: .35,
            3.67: .19,
            2.4: .04
        }

        increase = 0

        for average in increases:
            if gpa >= average:
                increase = increases[average]
                break

        return gpa + increase
