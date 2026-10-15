



# Library system for bookclub

# The database has 3 collections: Members, Books and Loans.
# Members handles memberdata and credentials for access.
# Books handles info about the books and how many copies the library has aswell as storing the reviews.
# Loans keeps track of which books are borrowed or returned and when.



from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["library"]



books = [
    {"_id": 1, "title": "brave new world", "author": "Aldous Huxley", "pages" : 525, "genre": "fiction", "year" : 1946},
    {"_id": 2, "title": "1984", "author": "George Orwell", "pages" : 480, "genre": "fiction", "year" : 1944},
    {"_id": 3, "title": "the angel of darkness", "author": "Caleb Carr", "pages" : 625, "genre": "fiction", "year" : 1999},
    {"_id": 4, "title": "the trial", "author": "Franz Kafka", "pages" : 270, "genre": "fiction", "year" : 1951},
    {"_id": 5, "title": "the transformation", "author": "Franz Kafka", "pages" : 70, "genre": "fiction", "year" : 1946},
    {"_id": 6, "title": "problems of knowledge", "author": "Michael Williams", "pages" : 200, "genre": "non fiction", "year" : 2011},
    {"_id": 7, "title": "the principles of morals", "author": "David Hume", "pages" : 260, "genre": "non fiction", "year" : 1751},
    {"_id": 8, "title": "group dynamics", "author": "Donelson R. Forsyth", "pages" : 667, "genre": "non fiction", "year" : 2012},
    {"_id": 9, "title": "business reseach methods", "author": "Emma Bell", "pages" : 600, "genre": "non fiction", "year" : 2018}
    ]





def main():
    print("Library System for Bookclub")

