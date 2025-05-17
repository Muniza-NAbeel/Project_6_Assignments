class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print(f"Teacher Name : Sir {self.name}, Subject : {self.subject}")

teacher = Teacher("Bilal Muhammad Khan", "Python")
teacher.display()