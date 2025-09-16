from course.course import Course
from department.department import Department
from student.student import Student

class LectureCourse(Course):
    def __init__(self,
                 name: str,
                 department: Department,
                 credit_hours: int,
                 capacity: int,
                 current_enrollment: int,
                 lecture_hall: str):
        super().__init__(name,
                         department,
                         credit_hours,
                         capacity,
                         current_enrollment)

        if len(lecture_hall.strip()) == 0:
            raise ValueError("Lecture hall must not be blank")

        self.__lecture_hall = lecture_hall

    def enroll_student(self, student: Student) -> str:
        message = f"{student.name}"
        buffer = int(self._capacity * .10)
        if self._current_enrollment < (self._capacity + buffer):
            self._current_enrollment += 1
            message += f" has been successfully enrolled in {self.name}"
        else:
            message += (" has NOT BEEN ENROLLED IN LECTURE: " +
                        f"{self.name} due to insufficient capacity.")
        return message;

    def __str__(self) -> str:
        return (
            super().__str__() +
            "\n" +
            f"Lecture Hall: {self.__lecture_hall}"
        )
