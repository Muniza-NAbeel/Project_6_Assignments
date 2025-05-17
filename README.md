🐍 Python OOP Assignments 🚀

📚 Table of Contents

1. Using self 👤
Create a Student class with name and marks attributes. Use self to initialize them via a constructor. Add a display() method to print student details.

2. Using cls 🏷️
Create a Counter class that tracks how many objects have been created using a class variable and a class method.

3. Public Variables and Methods 🚗
Create a Car class with a public variable brand and a public method start(). Instantiate and access them from outside the class.

4. Class Variables and Class Methods 🏦
Create a Bank class with a class variable bank_name. Add a class method change_bank_name(cls, name) that changes the bank name for all instances.

5. Static Variables and Static Methods ➕
Create a MathUtils class with a static method add(a, b) that returns the sum without using class or instance variables.

6. Constructors and Destructors 🛠️🗑️
Create a Logger class that prints a message when an object is created and another when it is destroyed.

7. Access Modifiers: Public, Private, and Protected 🔐
Create an Employee class with:

Public variable name

Protected variable _salary

Private variable __ssn

Try accessing all three and observe the behavior.

8. The super() Function 🧑‍🏫
Create a Person class and inherit Teacher from it. Use super() to call the base constructor and add a subject field in Teacher.

9. Abstract Classes and Methods 📐
Use the abc module to create an abstract class Shape with an abstract method area(). Implement Rectangle class that defines area().

10. Instance Methods 🐕
Create a Dog class with name and breed. Add an instance method bark() that prints a message including the dog's name.

11. Class Methods 📚
Create a Book class with a class variable total_books. Add a class method to increment this count when a new book is added.

12. Static Methods 🌡️
Create a TemperatureConverter class with a static method celsius_to_fahrenheit(c) that converts Celsius to Fahrenheit.

13. Composition 🏎️🔧
Create Engine and Car classes. Pass an Engine object to Car via constructor. Access an Engine method from Car.

14. Aggregation 🏢👔
Create Department and Employee classes. Department holds a reference to Employee, which exists independently.

15. Method Resolution Order (MRO) and Diamond Inheritance 🔄💎
Create classes A, B(A), C(A), and D(B, C). Override a method show() in B and C. Call show() from an instance of D to see MRO.

16. Function Decorators 🎨
Write a function decorator log_function_call that prints a message before the function runs. Apply it to a sample function.

17. Class Decorators 🎭
Create a class decorator add_greeting that adds a greet() method returning "Hello from Decorator!". Apply to class Person.

18. Property Decorators: @property, @setter, and @deleter 🏷️
Create a Product class with private attribute _price. Use property decorators to get, set, and delete the price.

19. callable() and __call__() 🎯
Create a Multiplier class with a factor set in __init__. Define __call__() to multiply input by the factor. Test with callable() and function call syntax.

20. Creating a Custom Exception ⚠️
Create a custom exception InvalidAgeError. Write check_age(age) that raises it if age < 18. Handle with try-except.

21. Make a Custom Class Iterable 🔢
Create a Countdown class that counts down from a start number to zero. Implement __iter__() and __next__() to make it iterable in a loop.

👤 Author :
Muniza Nabeel
Aspiring Web Developer & Python Enthusiast
