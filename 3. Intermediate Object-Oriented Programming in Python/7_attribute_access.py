class Student:
    def __init__(self, student_name, major):
        self.student_name = student_name
        self.major = major

    """
    This method is executed when an attempt to reference ANY attribute outside of an object's namespace is made.
    Implements custom functionality rather than raising and AttributeError
    """
    def __getattr__(self, name):
        print(f"'{name}' doesn't exist in this object's namespace, try setting a value for '{name}' first.")
        # We can use __getattr__ and __setattr__ together
        self.__setattr__(name, None)

    """
    This magic method is executed when a (new or existing) attribute is set or updated, include the use of __init__,
    uses __dict__ to create/update the attribute.
    """
    def __setattr__(self, name, value):
        # If value is a string, set the attribute using the __dict__ attribute
        if isinstance(value, str):
            print(f"Setting '{name}' = '{value}'")
            self.__dict__[name] = value
        elif value is None:
            print(f"Setting placeholder for '{name}' (None)")
            self.__dict__[name] = value
        else: # Otherwise, raise an exception noting an incorrect data type
            raise Exception('Unexpected data type!')


karina = Student('Karina', 'Literature')
karina.residence_hall   # Attempt to access an attribute that does not exist
karina.residence_hall = 'Honors College South'
print(karina.residence_hall)
try:
    karina.student_id = 123456
except Exception as e:
    print(e)