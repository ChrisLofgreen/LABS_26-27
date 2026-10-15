



# Library system for bookclub

# The database has 3 collections: Members, Books and Loans.
# Members handles memberdata and credentials for access.
# Books handles info about the books and how many copies the library has aswell as storing the reviews.
# Loans keeps track of which books are borrowed or returned and when.



from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["library"]


'''
books = [
    {"_id": 1, "title": "brave new world", "author": "Aldous Huxley", "genre": "fiction", "copies" : 2, "reviews": []},
    {"_id": 2, "title": "1984", "author": "George Orwell", "genre": "fiction", "copies" : 3, "reviews": []},
    {"_id": 3, "title": "the angel of darkness", "author": "Caleb Carr", "genre": "fiction", "copies" : 5, "reviews": []},
    {"_id": 4, "title": "the trial", "author": "Franz Kafka", "genre": "fiction", "copies" : 2, "reviews": []},
    {"_id": 5, "title": "the transformation", "author": "Franz Kafka", "genre": "fiction", "copies" : 2, "reviews": []},
    {"_id": 6, "title": "problems of knowledge", "author": "Michael Williams", "genre": "non fiction", "copies" : 1, "reviews": []},
    {"_id": 7, "title": "the principles of morals", "author": "David Hume", "genre": "non fiction", "copies" : 3, "reviews": []},
    {"_id": 8, "title": "group dynamics", "author": "Donelson R. Forsyth", "genre": "non fiction", "copies" : 1, "reviews": []},
    {"_id": 9, "title": "business reseach methods", "author": "Emma Bell", "genre": "non fiction", "copies" : 2, "reviews": []}
    ]

db.books.insert_many(books)
'''



def borrow():
    pass

def statistics():
    pass

def register():
    pass

def change_email():
    pass

def check_user_input_menu(user_input):
    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        print("\nOnly one single number, please try again")


def members():
    
    while True:

        print(f"\nType an option (number):\n\n1. Register as a member | 2. Change e-mail | 0. Exit to main menu")

        user_input = input()
        user_input = check_user_input_menu(user_input)

        if user_input == 1:
            print(register())
        elif user_input == 2:
            print(change_email()) 
        elif user_input == 0:
            break


def main():
    print("Library System for Bookclub")

    while True:

        print(f"\nType an option (number):\n\n1. Members | 2. Borrow (members only) | 3. Statistics | 0. Quit")

        user_input = input()
        user_input = check_user_input_menu(user_input)

        if user_input == 1:
            print(members())
        elif user_input == 2:
            print(borrow())
        elif user_input == 3:
            print (statistics())  
        elif user_input == 0:
            print ("\nExiting program\n")
            break


if __name__ == '__main__':
    main()