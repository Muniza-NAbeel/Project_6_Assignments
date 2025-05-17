class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        print("Car is starting...")
        return self.engine.start()

# Creating an instance of Engine
my_engine = Engine()
my_car = Car(my_engine)

# Using the Car class to start the engine
my_car.start_car()