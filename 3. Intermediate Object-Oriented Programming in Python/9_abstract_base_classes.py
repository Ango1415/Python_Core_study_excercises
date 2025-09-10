from abc import ABC, abstractmethod

class School(ABC):
    @abstractmethod
    def enroll(self):
        # This method must be implemented in classes that inherit from it
        pass

    @abstractmethod
    def add_course(self, course_name):
        pass

    # Concrete methods are inherited
    @staticmethod
    def graduate():
        print('Congrats on graduating!')

class HighSchool(School):
    def __init__(self):
        self.courses = []

    # Implementing abstract method
    def enroll(self):
        print('Welcome to High School')

    # Implementing abstract method
    def add_course(self, course_name):
        self.courses.append(course_name)
        print(f'You enrolled in {course_name}')

# Create an instance of HighSchool
high_school = HighSchool()
high_school.enroll()
high_school.graduate()