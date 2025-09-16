__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from student.student import Student
from department.department import Department
from course import *


def main():
    # Given students populated into a list.
    students = []
    student_number = 1000
    for i in range(10):
        name = "Student" + str(i)
        student_number += 1
        try:
            student = Student(student_number, name, Department.COMPUTER_SCIENCE )
            students.append(student)
        except ValueError as e:
            print(e)

    #1. Create an instance of the Course class with valid inputs.
    # If an exception occurs, print the exception instance.
    # Comment out once tested.
    try:
        isd = Course("ISD", Department.COMPUTER_SCIENCE, 6, 20, 0)
        print(isd)
    except TypeError as e:
        print(e)


    #2. Define a Lecture Course with a capacity of 20 and a current enrollment of 19
    # Use any valid values for the other parameters.
    # print the object
    try:
        isd = LectureCourse("ISD", Department.COMPUTER_SCIENCE, 6, 20, 19, "William Hall")
        print(isd)
    except ValueError as e:
        print(e)



    #3. Define a Lab Course with a capacity of 20 and a current enrollment of 8
    # Use any valid values for the other parameters.
    # print the object.
    try:
        med = LabCourse("Chemistry", Department.MEDICINE, 6, 20, 8, "Goggles")
        print(med)
    except ValueError as e:
        print(e)


    #4. Using a loop, enroll the students from the students list above
    # into the lecture course defined above.  Print the message returned
    # from the enroll_student method.
    for student in students:
        print(isd.enroll_student(student))



    #5. Using a loop, enroll the students from the students list above
    # into the lab course defined above.  Print hte message returned from
    # the enroll_student method.
    for student in students:
        print(med.enroll_student(student))



if __name__ == "__main__":
    main()


