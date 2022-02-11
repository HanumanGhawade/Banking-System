
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print(f"Name of the user is {self.name}")
        print(f"Age of the user is {self.age}")
        print(f"Gender of the user is {self.gender}")


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self .balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print('The account balance has been Updated', self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Fund / Available Balance Fund", self.balance)
        else:
            self.balance = self.balance-self.amount
            print("The Account has been Updated", self.balance)

    def view_balance(self):
        self.show_details()
        print('The Account has been updated', self.balance)


# user = User('Hanuman', 27, 'Male')
# user.show_details()
bank = Bank("Hanuman", 27, "Male")
bank.show_details()
bank.deposit(10000)
bank.withdraw(7000)
bank.view_balance()
