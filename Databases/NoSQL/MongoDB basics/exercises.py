



# Exercises: MongoDB Basics


from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


# 1.
'''
for product in db.products.find({"category": "Accessories"}):
    print(product["name"])
'''

# 2.
'''
for customer in db.customers.find({"city": "Göteborg"}):
    print(customer["first_name"], customer["last_name"])
'''

# 3.
'''
for product in db.products.find({}):
    print(product["name"], ":", product["price"])
'''

# 4.
'''
result = db.customers.count_documents({"city": "Uppsala"})
print(result)
'''

# 5.
'''
product = db.products.find_one({"name": "Sandals"})
print(product["stock"])
'''

# 6.
'''
for customer in db.customers.find({"newsletter": True}):
    print(customer["first_name"])
'''