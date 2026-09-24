



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

# Part G
'''
# 1-4.

class CPU:
    def __init__(self, model):
        self.model = model

class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu


cpu = CPU("9700 X")

computer = Computer("Asus", cpu)

print(computer.brand)
print(computer.cpu.model)
'''
# 5.

# It makes more sense since it is true in a very boolean sense :) There is a case to be made that you could make a "computer" without
# what we call a CPU today, but it is not true that a computer in the modern sense IS-A CPU, the CPU is a part of what makes up a computer.
# Therefor the computer HAS-A CPU, like it HAS-A Case, a motherbord (That in turn might have a CPU socket) etc.

# 6.

# Car HAS-An Engine, Phone IS-A Device, then it becomes a bit more complicated since:
# Course HAS-A Teacher, but Teacher also HAS-A Course - but none of them IS the other.
# Next level of complexity: Manager HAS-An Employee (one could say). But it's also likley that Manager IS-An Employee.

# So in the more complex cases it matters what the program is supposed to do, or to be more precise:
# What structure the code is supposed to manifest.


# Part H

class Exporter:
    def __init__(self):
        pass

    def export(self, data):
        self.data = data
        return data


class ConsoleExporter(Exporter):
    def __init__(self):
        pass

    def export(self, data):
        self.data = data
        master_addon = super().export(data) + " being processed by the Console exporter"
        return master_addon

    def __str__(self):
        return "This is a console exporter"

    
class TextExporter(Exporter):
    def __init__(self):
        pass

    def export(self, data):
        self.data = data
        master_addon = super().export(data) + " being processed by the Text exporter"
        return master_addon

    def __str__(self):
        return "This is a text exporter"


class SummeryExporter(Exporter):
    def __init__(self):
        pass

    def export(self, data):
        self.data = data
        master_addon = super().export(data) + " being processed by the Summery exporter"
        return master_addon

    def __str__(self):
            return "This is a Summery exporter"

class AnotherExporter:
    def __init__(self):
        pass

    def export(self, data):
        self.data = data
        another_addon = data + " being processed by Another exporter"
        return another_addon



ex1 = ConsoleExporter()
ex2 = TextExporter()
ex3 = SummeryExporter()
ex4 = AnotherExporter()
data1 = "I am"

list_of_objects = []

list_of_objects.append(ex1)
list_of_objects.append(ex2)
list_of_objects.append(ex3)
list_of_objects.append(ex4)

for object in list_of_objects:
    exporter_status = ""

    if isinstance(object, Exporter) == True:
        exporter_status = " "
    else:
        exporter_status = " NOT "

    print(f"{object.export(data1)}, which is{exporter_status}an instance of the Exporter parent class")

