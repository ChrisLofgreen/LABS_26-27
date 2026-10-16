



# Library system for bookclub

# The database has 3 collections: Members, Books and Loans.
# Members handles memberdata and credentials for access.
# Books handles info about the books and how many copies the library has aswell as storing the reviews.
# Loans keeps track of which books are borrowed or returned and when.



from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["library"]

import time
import re


books = [
    {"_id": 1, "title": "brave new world", "author": "Aldous Huxley", "genre": "fiction", "copies" : 2, "reviews": [], "search": ["brave", "new", "world", "aldous", "huxley", "fiction"]},
    {"_id": 2, "title": "1984", "author": "George Orwell", "genre": "fiction", "copies" : 3, "reviews": [], "search": ["1984", "george", "orwell", "fiction"]},
    {"_id": 3, "title": "the angel of darkness", "author": "Caleb Carr", "genre": "fiction", "copies" : 5, "reviews": [], "search": ["the", "angel", "of", "darkness", "caleb", "carr", "non fiction"]},
    {"_id": 4, "title": "the trial", "author": "Franz Kafka", "genre": "fiction", "copies" : 2, "reviews": [], "search": ["the", "trial", "franz", "kafka", "fiction"]},
    {"_id": 5, "title": "the transformation", "author": "Franz Kafka", "genre": "fiction", "copies" : 2, "reviews": [], "search": ["the", "transformation", "franz", "kafka", "fiction"]},
    {"_id": 6, "title": "problems of knowledge", "author": "Michael Williams", "genre": "non fiction", "copies" : 1, "reviews": [], "search": ["problems", "of", "knowledge", "michael", "williams", "non fiction"]},
    {"_id": 7, "title": "the principles of morals", "author": "David Hume", "genre": "non fiction", "copies" : 3, "reviews": [], "search": ["the", "principles", "of", "morals", "david", "hume", "non fiction"]},
    {"_id": 8, "title": "group dynamics", "author": "Donelson R. Forsyth", "genre": "non fiction", "copies" : 1, "reviews": [], "search": ["group", "dynamics", "donelson", "forsyth", "non fiction"]},
    {"_id": 9, "title": "business reseach methods", "author": "Emma Bell", "genre": "non fiction", "copies" : 2, "reviews": [], "search": ["business", "reseach", "methods", "emma", "bell", "non fiction"]}
]

db.books.insert_many(books)

'''
db.members.insert_one({"first_name": "John", "last_name": "Test", "email": "john@test.com", "borrowed_books": [], "overdue": False})
'''


def check_user_input_menu(user_input):
    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        print("\nOnly one single number, please try again")


def register():
    
    print(f"\nEnter First name:")
    first_name = input().strip()
    print(f"\nEnter Last name:")
    last_name = input().strip()
    if str(first_name.replace(" ","") + last_name.replace(" ","")).isalpha():
        pass
    else:
        print("only a-z, A-Z in name please! Blank space between double names")
        time.sleep(1)
        register()

    print(f"\nEnter valid email adress:")
    email = input()

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    valid = re.match(pattern, email)

    if valid:
        pass
    else:
        print("That doesnt seem like a valid e-mail address, try again")
        register()
        
    match_test = db.members.find_one({"email": email}, {"email": 1, "_id": 0})
    if match_test == None:
        pass
    else:
        print("The e-mail you provided has already been registered, you can try again after a short wait")
        time.sleep(2)
        main()

    db.members.insert_one({
        "first_name": first_name, 
        "last_name": last_name, 
        "email": email, 
        "borrowed_books": [], 
        "overdue": False
    })

    return "You have been added to the bookclub library. Best of luck with your journey through the world of literature!"


def search_books():
    pass


def borrow_books():
    pass


def return_books():
    pass


def change_email():
    print("You need to type all your credentials to change e-mail address. Do you want to continue? (Y to continue, anything else to quit):")
    user_input = input()
    
    if user_input == "Y" or user_input == "y":
        pass
    else:
        members()


def members():
    
    while True:

        print(f"\nType an option (number):\n\n1. Register as a member | 2. Change e-mail | 0. Exit to main menu")

        user_input = check_user_input_menu(input())

        if user_input == 1:
            print(register())
        elif user_input == 2:
            print(change_email()) 
        elif user_input == 0:
            break


def books():

    while True:

        print(f"\nType an option (number):\n\n1. Search for books to borrow | 2. Return books | 0. Exit to main menu")

        user_input = check_user_input_menu(input())

        if user_input == 1:
            print(search_books())
        elif user_input == 2:
            print(return_books()) 
        elif user_input == 0:
            break


def statistics():
    pass


def main():
    print("Library System for Bookclub")

    while True:

        print(f"\nType an option (number):\n\n1. Members | 2. Books (membership required) | 3. Statistics | 0. Quit")

        user_input = check_user_input_menu(input())

        if user_input == 1:
            print(members())
        elif user_input == 2:
            print(books())
        elif user_input == 3:
            print (statistics())  
        elif user_input == 0:
            print ("\nExiting program\n")
            break


if __name__ == '__main__':
    main()