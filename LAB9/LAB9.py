



# Part E
'''
# 1-5.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"


product1 = Product("Momin cup", 150)
product2 = Product("Mad hatter's hat", 1500)
product3 = Product("T-1000's sunglasses", 75)

# print(product1)
# print(product2)
# print(product3)

product2_str = str(product2)

print(product2_str)
'''

# Part F

# 1-5.
'''
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"\nThis is an account.\n\nOwner: {self.owner}\nBalance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)

        self.interest_rate = interest_rate

    def __str__(self):
        return f"{super().__str__()}\nInterest Rate: {self.interest_rate}\n"

account1 = Account("Ronnie", 1000)
s_account1 = SavingsAccount("Lizzy", 2000, "2%")

print(account1)
print(s_account1)
'''

