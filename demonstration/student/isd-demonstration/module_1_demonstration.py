__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1. Import as necessary.
from course.course import Course
from department.department import Department

def main():
    # 1. Create an instance of the Course class with valid inputs.
    #    Print the instance.
    #    If an exception occurs, print the exception instance.
    try:
        course = Course("ISD", Department.COMPUTER_SCIENCE, 6)
        print(course)
    except ValueError as e:
        print(e)

    # 2. Create an instance of the Course class with invalid inputs.
    # Print the instance.
    # If an exception occurs, print the exception instance.
    try:
        invalid = Course("ISD", "Invalid Department", 6)
        print(invalid)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()


