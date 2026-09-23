



# Part C
'''
# 1-3.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class SavingsAccount(Account):

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

# 4.
savings1 = SavingsAccount("Anna", 1000, 0.02)
savings2 = SavingsAccount("Conny", 100, 0.015)

print(savings1.owner, savings1.balance, savings1.interest_rate)
print(savings2.owner, savings2.balance, savings2.interest_rate)

# 5.
# A savings account is an account :) And the structure is useful since the person might have many different engagements with the bank,
# the savings account beeing just one of them. But maybe balance should really be at the level of SavingsAccount in this case.
'''


# Part D

# 1-3.
'''
class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return f"{self.name} is a "


class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.languages = []

    def get_information(self):
        print (super().get_information() + "developer. They can code in:")
        for index, language in enumerate(self.languages, start=1):
            print(f"{index}. {language}")
        return ""

    def add_language(self, language):
        self.languages.append(language)


class RacingDriver(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.techniques = []

    def get_information(self):
        print (super().get_information() + "racing driver. They know the following techniques:")
        for index, technique in enumerate(self.techniques, start=1):
            print(f"{index}. {technique}")
        return ""
    
    def add_technique(self, technique):
        self.techniques.append(technique)


developer1 = Developer("Jimmy")
developer1.add_language("Python")
developer1.add_language("C")

driver1 = RacingDriver("Anna")
driver1.add_technique("Threshold breaking")
driver1.add_technique("Slipstreaming")

# 4.
print(developer1.get_information())
print(driver1.get_information())

# 5.

employee1 = Employee("?")
# employee1.add_language("C#") Returns AttributeError: 'Employee' object has no attribute 'add_language'
'''

# Part E
'''
# 1-4.

class Device:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.is_functional = True

        if self.year < 0:
            raise ValueError ("year cannot be a negative value")


class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)
        self.ram_gb = ram_gb

class Desktop(Device):
    def __init__(self, brand, year):
        super().__init__(brand, year)


laptop1 = Laptop("Apple", 2025, 16) # raises ValueError: year cannot be a negative value
desktop1 = Desktop("Asus", 2026)

# 5.

print (desktop1.is_functional)
print (laptop1.is_functional)

#laptop1 = Laptop("Apple", -2025, 16) # raises ValueError: year cannot be a negative value
#desktop1 = Desktop("Asus", -2026) # raises ValueError: year cannot be a negative value
'''