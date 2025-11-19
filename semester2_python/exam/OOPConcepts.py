class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Customer(Person):
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self.customer_id = customer_id

    def __str__(self):
        return f"{super().__str__()}, Customer ID: {self.customer_id}"


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"{self.balance}")

    def __str__(self):
        return f"Balance: ${self.balance}"


bank_account = BankAccount(200)
bank_account.deposit(90)

print(f"Bank Account: {bank_account}")
