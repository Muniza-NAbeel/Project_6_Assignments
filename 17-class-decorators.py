def add_greeting(cls):  # Class decorator to modify a class
    class WrappedClass(cls):  # New class inheriting the original class
        def greet(self):  # Add a new method greet()
            return "Hello from Decorator!"  # Return fixed greeting
    return WrappedClass  # Return modified class

@add_greeting  # Apply the decorator to Person class
class Person:  # Original class definition
    pass  # No additional functionality

person = Person()  # Create an object of the Person class
print(person.greet())  # Call the added greet() method
