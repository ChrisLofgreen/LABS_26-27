



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

# 7.
'''
new_customer = db.customers.insert_one({
    "first_name": "Christofer",
    "last_name": "Löfgreen",
    "email": "ch@lo.com",
    "city": "Stockholm",
    "phone": "070-1234567"
})

print(new_customer.inserted_id)

from pprint import pprint

result = db.customers.find_one({"email": "ch@lo.com"})
pprint(result)
'''

# 8.
'''
new_products = db.products.insert_many([
    {"_id": 13, "name": "Rustic Cane", "category": "Accessories", "price": 599, "stock": 1, "tags": ["outdoors"]},
    {"_id": 14, "name": "Beaver Cap", "category": "Accessories", "price": 399, "stock": 20, "tags": ["novelty"], "details": {"color": "brown"}}
])

print(db.products.count_documents({}))
'''

# 9.
'''
for customer in db.customers.find():
    print(f"{customer["first_name"]} {customer["last_name"]} ({customer.get("city", "unknown")})")
'''

# 10.
'''
for order in db.orders.find():
    if len(order["items"]) == 1:
        print(f"Order {order["_id"]}: {len(order["items"])} item")
    else:
        print(f"Order {order["_id"]}: {len(order["items"])} items")
'''