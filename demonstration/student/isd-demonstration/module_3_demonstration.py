__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from student.student import Student
from department.department import Department
from course import *
from patterns.decorator import *

def main():
    # Given students populated into a list.
    students = []

    students.append(Student("John Brunelle", Department.MEDICINE))
    students.append(Student("Elizabeth Sinclair", Department.COMPUTER_SCIENCE))
    students.append(Student("Angela Brock", Department.EDUCATION))
    students.append(Student("Robert Flammand", Department.MEDICINE))
    students.append(Student("Arthur Armstrong", Department.COMPUTER_SCIENCE))
    students.append(Student("Chris Mullin", Department.EDUCATION))
    students.append(Student("Jackie Blanchard", Department.MEDICINE))
    students.append(Student("George Shanahan", Department.COMPUTER_SCIENCE))
    students.append(Student("Linda Eck", Department.EDUCATION))
    students.append(Student("Judy Gardener", Department.MEDICINE))
    students.append(Student("Donna Smith", Department.COMPUTER_SCIENCE))
    students.append(Student("Eric Best", Department.EDUCATION))


    for student in students:
        print(f"\n{str(student)}")

        ### DECORATOR ###
        print("Original Grade Point Average: ", student.grade_point_average)

        volunteer_student = VolunteerDecorator(student)
        print("GPA with volunteer boost: ", volunteer_student.grade_point_average)
        council_student = CouncilDecorator(student)
        print("GPA with student council boost: ", council_student.grade_point_average)


if __name__ == "__main__":
    main()


