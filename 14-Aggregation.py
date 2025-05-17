class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f" Employee Name : {self.name}"
    
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

    def get_details(self):
        return f" Department Name : {self.dept_name}\n{self.employee.get_details()}"
    
emp = Employee("Muniza Nabeel")
dept = Department("Software Engineering", emp)
print(dept.get_details())