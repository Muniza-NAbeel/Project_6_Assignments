class Logger:
    def __init__(self):
        print("Logger Object Created . ")

    def __del__(self):
        print("Logger Object Destructed . ")

# Create an instance of Logger
log = Logger()

# Use the logger instance
print("Logging some information...")
del log