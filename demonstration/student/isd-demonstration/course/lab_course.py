from course.course import Course
from department.department import Department
from student.student import Student

class LabCourse(Course):

    def __init__(self,
                 name: str,
                 department: Department,
                 credit_hours: int,
                 capacity: int,
                 current_enrollment: int,
                 lab_equipment: str):
        super().__init__(name,
                         department,
                         credit_hours,
                         capacity,
                         current_enrollment)

        if not lab_equipment.strip():
            lab_equipment = "None"

        self.__lab_equipment = lab_equipment


    def enroll_student(self, student: Student) -> bool:
        message = f"{student.name}"
        if self._current_enrollment < (self._capacity / 2):
            self._current_enrollment += 1
            message += " has been successfully enrolled"
        else:
            message += (f" HAS NOT BEEN ENROLLED IN LAB: {self.name}" +
                        "due to insufficient capacity.")
        return message
    def __str__(self) -> str:
        return (
            super().__str__() +
            f"\nRequired Equipment: {self.__lab_equipment}"
        )