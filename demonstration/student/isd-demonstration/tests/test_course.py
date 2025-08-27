"""Unit tests for the Course class.

Author: ACE Faculty
Modified by: Allendale Nato
Date: Aug 26, 2025
Usage:
    To execute all tests in the terminal execute
    the following command (replace test_file_name.py with
    the appropriate file name.):
        python -m unittest tests/test_file_name.py
"""
import unittest
from department.department import Department
from course.course import Course


class TestCourse(unittest.TestCase):
    def setUp(self) -> None:
        self.course = Course("ISD", Department.COMPUTER_SCIENCE, 6)

    def test_init_valid(self) -> None:
        # Arrange
        name = "ISD"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 6

        # Act
        course = Course(name, department, credit_hours)

        # Assert
        self.assertEqual(name, course._Course__name)
        self.assertEqual(department, course._Course__department)
        self.assertEqual(credit_hours, course.credit_hours)

    def test_init_raise_valueerror_blank_name(self) -> None:
        # Arrange
        name = ""
        department = Department.COMPUTER_SCIENCE
        credit_hours = 6

        # Act
        with self.assertRaises(ValueError) as context:
            Course(name, department, credit_hours)

        # Assert
        expected = "Name connot be blank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_invalid_name_raises_exception(self) -> None:
        # Arrange
        name = ""
        department = Department.COMPUTER_SCIENCE
        credit_hours = 6

        # Act
        with self.assertRaises(ValueError):
            Course(name, department, credit_hours)

    def test_init_raise_valueerror_invalid_department(self) -> None:
        # Arrange
        name = "ISD"
        department = "PHARMACY"
        credit_hours = 6

        # Act
        with self.assertRaises(ValueError) as context:
            Course(name, department, credit_hours)

        # Assert
        expected = "Department is invalid."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_raise_valueerror_nonnumeric_credit_hours(self) -> None:
        # Arrange
        name = "ISD"
        department = Department.COMPUTER_SCIENCE
        credit_hours = "6"

        # Act
        with self.assertRaises(ValueError) as context:
            Course(name, department, credit_hours)

        # Assert
        expected = "Credit hours must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_name_returns_current_state(self) -> None:
        # Act & Assert
        expected = "ISD"
        actual = self.course.name
        self.assertEqual(expected, actual)

    def test_department_returns_current_state(self) -> None:
        # Act & Assert
        expected = Department.COMPUTER_SCIENCE
        actual = self.course.department
        self.assertEqual(expected, actual)

    def test_credit_hours_returns_current_state(self) -> None:
        # Act & Assert
        expected = 6
        actual = self.course.credit_hours
        self.assertEqual(expected, actual)

    def test_str_prints_valid_sting_representation(self) -> None:
        # Arrange
        name = "ISD"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 6
        expected = (
            f"Course: {name}\n"
            "Department: Computer Science\n"
            f"Credit Hours: {credit_hours}"
        )

        # Act
        course = Course(name, department, credit_hours)

        # Assert
        actual = course.__str__()
        self.assertEqual(expected, actual)

