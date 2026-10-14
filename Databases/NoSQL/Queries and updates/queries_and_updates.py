


# Exercises: Queries and updates


from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 1.
'''
for product in db.products.find({"price": {"$gt": 1000}}):
    print(product["name"], product["price"])
'''
# 2.
'''
for order in db.orders.find({"status": {"$ne": "delivered"}}):
    print(order["_id"], order["status"])
'''
# 3.
'''
from pprint import pprint

for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
    pprint(customer)
'''
# 4.
'''
from pprint import pprint

for product in db.products.find({"details.color": "white"}):
    pprint(product)
'''