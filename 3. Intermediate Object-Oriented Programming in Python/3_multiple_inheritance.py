class Employee:
    def __init__(self, department):
        self.department = department

    def begin_job(self):
        print(f"Welcome to {self.department}")

class Student:
    def __init__(self, school):
        self.school = school
        self.courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)

class Intern(Employee, Student):
    def __init__(self, department, school, duration):
        # Make a call to BOTH constructors
        Employee.__init__(self, department)
        Student.__init__(self, school)
        self.duration = duration

    def onboard(self, mentor):
        # Implementation of a new method
        pass


stephen = Intern('Software Development', 'Echo University', 10)
stephen.begin_job() # Method for Employee

stephen.add_course('Intermediate OOP in Python')    # Method from Intern
print(stephen.courses)

"""
Method Resolution Order (MRO) - The order in which Python determines which method is used when parent and children
implement a method with the same name.
"""
# Find the MRO for Intern
print(Intern.mro())
print(Intern.__mro__)