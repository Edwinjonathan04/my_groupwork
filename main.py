
class Account:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            print("Insufficient funds!")
            return False

    def get_balance(self):
        return self._balance


class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        if amount <= 700000:
            super().deposit(amount)
            self._balance *= 1.005  # 0.5% interest
        else:
            print("Deposit limit exceeded for Savings Account!")


class CurrentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)


class ChildrensAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        super().deposit(amount)
        self._balance *= 1.007  # 0.7% interest

    def withdraw(self, amount):
        print("Withdrawal not allowed for Children's Account!")


class StudentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        if amount <= 50000:
            super().deposit(amount)
        else:
            print("Deposit limit exceeded for Student Account!")

    def withdraw(self, amount):
        if amount <= 2000:
            super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded for Student Account!")


# Example usage:
savings_acc = SavingsAccount()
savings_acc.deposit(100000)
print("Savings Account Balance:", savings_acc.get_balance())

current_acc = CurrentAccount()
current_acc.deposit(50000)
current_acc.withdraw(20000)
print("Current Account Balance:", current_acc.get_balance())

children_acc = ChildrensAccount()
children_acc.deposit(20000)
children_acc.withdraw(1000)  # Withdrawal should not be allowed
print("Children's Account Balance:", children_acc.get_balance())

student_acc = StudentAccount()
student_acc.deposit(30000)
student_acc.withdraw(5000)  # Withdrawal limit exceeded message should appear
print("Student Account Balance:", student_acc.get_balance())
