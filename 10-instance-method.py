class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):     # Instance method
        """Dog barking"""
        print(f"{self.name} is Barking !!")

my_pet = Dog("Puppy", "pomeranian")   # Creating object of Dog
my_pet.bark()  # Calling instance method