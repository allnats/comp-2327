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
    def test_init_valid(self):
        # Arrange
        name = "ISD"
        department = Department.COMPUTER_SCIENCE
        credit_hours = 6

        # Act
        course = Course(name, department, credit_hours)

        # Assert
        self.assertEqual(name, course._Course__name)
