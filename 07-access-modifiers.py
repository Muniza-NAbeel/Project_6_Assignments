class Employee:
    def __init__(self, name, salary, ssn):
        # Public Attribute
        self.name = name
        
        # Protected Attribute
        self._salary = salary

        # Private Attribute
        self.__ssn = ssn

emp = Employee("Muniza Nabeel", 50000, "123-45-6789")

# Accessing Public Attribute
print("Employee Name : ", emp.name)

# Accessing Protected Attribute
print("Employee Salary : ", emp._salary)   # This is not recommended but still possible

# Accessing Private Attribute
try:
    print("Employee SSN : ", emp.__ssn) # This will raise an AttributeError
except AttributeError as e:
    print("Error : ", e)    # This msg prints the error message