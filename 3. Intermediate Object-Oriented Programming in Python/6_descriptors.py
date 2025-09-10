class Student:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    @property
    def ssn(self): # This is the getter method
        return 'XXX-XX-' + self._ssn[-4:]   # I think we must use _ssn to avoid the getter method itself

    @ssn.setter
    def ssn(self, new_ssn):
        # We can add things such as data validation, operations on others attributes, etc.
        if len(new_ssn) == 11:
            self._ssn = new_ssn     # Again we use _ssn, I think with this we access directly to the attribute

    @ssn.deleter
    def ssn(self):
        # Can perform clean up, soft delete, raise exception
        raise AttributeError("Can't delete SSN")


shaw = Student('Daniel Shaw', '193-80-1821')
print(shaw.ssn)

shaw.ssn = '821-11-9380'
print(shaw.ssn)

try:
    del shaw.ssn
except AttributeError as ate:
    print(ate)