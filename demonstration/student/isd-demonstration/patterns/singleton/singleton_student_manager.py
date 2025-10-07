"""Student ID Singleton."""

__author__ = "Allendale Nato"
__version__ = "1.0.0"

class SingletonStudentManager:
    """Represents a Singleton Manager for Student IDs.

    Student singleton pattern to ensure only one instance of the class
    is in memory at a given time.

    """

    __instance = None
    __next_student_number = 20240000

    def __new__(cls):
        """Construct the SingletonStudentManager in memory."""
        if not cls.__instance:
            # Create a new instance and return it
            cls.__instance = super(SingletonStudentManager, cls).__new__(cls)

        # return instance either or...
        return cls.__instance

    def get_next_student_number(self) -> int:
        """Return the next available student number."""
        student_number = self.__next_student_number
        self.__next_student_number += 1
        return student_number
