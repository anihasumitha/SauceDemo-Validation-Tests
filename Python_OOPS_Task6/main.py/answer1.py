class BankAccount:  # Main class

    def __init__(self, account_number, balance=0):  # Init constructor to initialize the attributes
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, deposited_amount):  # Method to deposit
        self.__balance += deposited_amount

    def withdraw(self, withdrawn_amount):  # Method to withdraw funds
        if withdrawn_amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= withdrawn_amount

    def get_balance(self):  # Method to get the current balance
        return self.__balance


class SavingsAccount(BankAccount):  # Child class
    def __init__(self, account_number, balance, interest_rate=0.12):
        super().__init__(account_number, balance)  # Inheriting attributes and methods from BankAccount
        self.interest_rate = interest_rate

    def calc_interest(self):  # Method to calculate interest
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)  # Use the deposit method to add interest
        return f"Interest applied. New balance: {self.get_balance()}"


class CurrentAccount(BankAccount):  # Child class
    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):  # Overriding the inherited withdraw method due to the min balance requirement
        if self.get_balance() - amount < self.min_balance:
            return f"Cannot withdraw! Minimum balance of {self.min_balance} required."
        super().withdraw(amount)  # Call the parent class withdraw method
        return f"Withdrawal successful. New balance: {self.get_balance()}"


# Testing the classes
bank_acc = BankAccount("767833883", 2000)
bank_acc.deposit(100)  # Deposits 100
print("Bank Account Balance:", bank_acc.get_balance())  # Check balance after deposit
print("Withdrawn Amount:", bank_acc.withdraw(100))  # Withdraws 100
print("Bank Account Balance:", bank_acc.get_balance())  # Check balance after withdrawal

savings_acc = SavingsAccount("94545422", 1000)
print(savings_acc.calc_interest())  # Apply interest
print("Savings Account Balance:", savings_acc.get_balance())  # Check balance after interest

current_acc = CurrentAccount("76234899", 2000, 500)
print(current_acc.withdraw(1600))  # Not allowed, exceeded min balance
print(current_acc.withdraw(1400))  # Allowed
print("Current Account Balance:", current_acc.get_balance())  # Check balance after withdrawal
