


# Exercises: Queries and updates


from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

from pprint import pprint

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
for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
    pprint(customer)
'''

# 4.
'''
for product in db.products.find({"details.color": "white"}):
    pprint(product)
'''

# 5.
'''
for product in db.products.find({"tags": "sport"}, {"name": 1, "tags": 1, "_id": 0}):
    pprint(product)
'''

# 6.
'''
for product in db.products.find({}, {"name": 1, "price": 1, "_id": 0}).sort("price", 1).limit(5):
    pprint(product)
'''

# 7.
'''
for order in db.orders.find({"items.product_id": 2}):
    print("Order:" ,order["_id"])
'''

# 8.
'''
db.products.update_many({"category": "Accessories"}, {"$inc": {"price": 20}})
for product in db.products.find({"category": "Accessories"}, {"name": 1, "price": 1, "_id": 0}):
    print(product["name"], ":",product["price"])
'''

# 9. 
'''
from datetime import datetime

db.products.update_one(
    {"_id": 11},
    {"$set": {"restock_date": datetime.now()}} |
    {"$push": {"tags": "new"}},
    upsert=True
    )


result = db.products.find_one({"_id": 11})
pprint(result)
'''

# 10.
'''
from datetime import datetime

result = db.orders.count_documents({"status": "new", "order_date": {"$lt": datetime(2026, 3, 20)}})
print("Document count:", result)

result = db.orders.delete_many({"status": "new", "order_date": {"$lt": datetime(2026, 3, 20)}})
print("Deleted count:", result.deleted_count)
'''


# Extras

# 1. make campaign-codes on products
'''
result = db.products.update_many(
    {"category": "Clothing"},
    {"$set": {"campaign-codes": [{"clothing_bonanza": 50}]}},
    upsert=True
    )

print(result)


result = db.products.update_one(
    {"_id": 2},
    {"$push": {"campaign-codes": {"t-shirt_bonanza": 20}}},
    upsert=True
    )

print(result)
'''


# 2. Look for active codes
'''
active_codes = []

for product in db.products.find({"campaign-codes": {"$exists": True}}):
    active_codes.append([product["_id"], product["campaign-codes"]])

print(active_codes)


for id in active_codes:
    print(f"Product: {id[0]} - Active Codes:")
    for code in id[1]:
        print (code)
    
    print("")
'''