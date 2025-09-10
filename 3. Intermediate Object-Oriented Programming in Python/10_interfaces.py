"""
These are abstract classes with all their methods being abstract.
"""
from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def assign_homework(self, assignment_number, due_date):
        pass

    @abstractmethod
    def grade_assignment(self, assignment_number):
        pass

class ProgrammingCourse(Course):
    def __init__(self, course_name):
        self.course_name = course_name

    def assign_homework(self, assignment_number, due_date):
        pass

    def grade_assignment(self, assignment_number):
        pass