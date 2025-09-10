from typing import List, Dict
"""
Information about an object, not enforced by the interpreter, can be used with built-in keywords, typing library or
custom classes
Other type hints: Any, Set, Iterator, Callable
"""
# When creating a variable
gpa: float = 3.92
names: List[str] = ['Morgan', 'Chuck', 'Anna']
gpas: Dict[str, float] = {
    'Casey': 3.71,
    'Sarah': 4.0
}

# Add to a func/meth definition
def get_schedule(semester: str) -> dict:
    pass

def check_grades(year:str) -> List[int]:
    pass

# Can even use custom classes
class Student:
    def __init__(self, name:str, student_id:int, tuition_balance:float)->None:
        self.name: str = name
        self.student_id: int = student_id
        self.tuition_balance: float = tuition_balance

    def get_course(self, course_id:str)->str:
        pass

students: Dict[str, Student] = {}
walker: Student = Student('Sarah Walker', 319921, 15000)
