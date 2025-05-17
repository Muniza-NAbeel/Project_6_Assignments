class Student: 
    def __init__(self, name, marks):                       # Ye constructor hai jo student ka name aur marks Initialize karta hai
        self.name = name                                   # Student ka name Initialize karega
        self.marks = marks                                 # Student ke marks Initialize karega
    
    def display(self):                                     # Ye method student ka name aur marks display karega
        print(f"Student_Name: {self.name}, Marks: {self.marks}")  

student = Student("Muniza Nabeel", 100)                            # Ek student ka object banaya hai
student.display()                                          # Student ka name aur marks display karne ke liye display method ko call kiya hai