
# Part B
'''
movie = {
    "title": "fire walk with me",
    "director": "David Lynch",
    "rating": 67
}

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_above_85(self):
        if self.rating > 85:
            return "It's above 85!"
        
        return "It's not above 85"

movie1 = Movie("fire walk with me", "David Lynch", 67)

# I would choose dictionary if when we don't need calculations within the class. In this case i would lean towards dictionary if this was
# all we needed to do because the "is_above_85" method could easily, and perhaps preferibly be a function iterating over a list of
# dictionaries or something like that. This method is not inherent to any object "Movie" but is better understood as a function to work 
# with a collection of movies. 
'''

    

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

# Part F
'''
# 1-4.

class Notification:
    def send(self):
        return "This is a test message, nothing to worry about"

class EmailNotification(Notification):
    def send(self):
        return "This is an E-Mail: The bombers are over the Baltic!"

class SMSNotification(Notification):
    def send(self):
        return "This is a SMS: Sorry... Those where seals... Our guys confused the terms 'sonar' and 'radar'.. Sorry"

message1 = Notification()
message2 = EmailNotification()
message3 = SMSNotification()

#print(message1.send())
#print(message2.send())
#print(message3.send())

# 5.

# On all three messages the send() method in class Notification is called. But the behaivior of send() is altered by the subsequent
# sub-class versions.

'''

# Part G
'''
# 1-3.

class Report:
    def get_summery(self):
        return "This is a general report summery:"

class SalesReport(Report):
    def get_summery(self):
        report_summery = super().get_summery() + "\n"

        return report_summery + "\nSales\nSales where really good!"

# 4.
salesreport1 = SalesReport()
print(salesreport1.get_summery())
'''

# Part H

# 1-9.
'''
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def change_username(self, new_username):
        if " " not in new_username:
            self.username = new_username
            return "username changed"

        raise ValueError("username cannot include blank spaces")

    def change_email(self, new_email):
        if "@" in new_email:
            self.email = new_email
            return "e-mail changed"

        raise ValueError("an e-mail adress must include @")

    def get_user_description(self):
        return "You are a general user"


class PremiumUser(User):
    def __init__(self, username, email, account_nr):
        super().__init__(username, email)

        self.account_nr = account_nr

    def get_user_description(self):
        general_info = super().get_user_description()

        return general_info + f" sort of. But you do have some special privilages. Your account number is: {self.account_nr}" 

    def get_account_nr(self):
        return self.account_nr
    

class AdminUser(User):
    def __init__(self, username, email):
        super().__init__(username, email)

        self.security_access = False

    def get_user_description(self):
        if self.security_access == True:
            return "You are an admin user with security access"
        
        return "You are an admin user, but you do not have security access"

    def implement_security_access(self):
        if self.security_access == True:
            return "Already have security access"

        self.security_access = True
        return "You now have security access! (A bit easy to get maybe...)"


user1 = User("anna_a", "anna@andersson.se")
premiumuser1 = PremiumUser("benny_b", "benny@bjornsson.se", 11111)
admin1 = AdminUser("carrie_c", "carrie@convinient.com")
admin1.implement_security_access()
admin2 = AdminUser("darryl_d", "darryl@donaldsson.com")

print(user1.get_user_description())
print(premiumuser1.get_user_description())
print(admin1.get_user_description())
print(admin2.get_user_description())

admin2.change_username("darril_d")
admin2.change_email("darril@donaldsson.nu")
print(admin2.username)
print(admin2.email)

'''

# 10.
# Both AdminUser and PremiumUser are users. The may have a little bit different info and privileges on top but under that
# they do need the basics for being a User, in this case a username and an email. And the fact that they can share functions
# like change_email() saves us from some duplicated code and update problems.