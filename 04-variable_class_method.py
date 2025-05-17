class Bank:
    bank_name = "State Bank"

    def __init__(self, branch):
        self.branch = branch

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Bank Name: {self.bank_name}, Branch: {self.branch}")

bank1 = Bank("Karachi")
bank2 = Bank("Lahore")

# Displaying initial bank details
print("Before changing bank name:")
bank1.display()
bank2.display()

# Changing the bank name using class method

Bank.change_bank_name("National Bank of Pakistan")
# Displaying bank details after changing the bank name
print("\nAfter changing bank name:")
bank1.display()
bank2.display()
