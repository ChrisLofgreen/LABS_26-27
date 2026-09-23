



# Part C

# 1.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

savings1 = SavingsAccount("Anna", 1000, 0.02)
savings2 = SavingsAccount("Conny", 100, 0.015)

print(savings1.owner, savings1.balance, savings1.interest_rate)
print(savings2.owner, savings2.balance, savings2.interest_rate)


# A savings account is an account :) And the structure is useful since the person might have many different engagements with the bank,
# the savings account beeing just one of them. But maybe balance should really be at the level of SavingsAccount in this case.

