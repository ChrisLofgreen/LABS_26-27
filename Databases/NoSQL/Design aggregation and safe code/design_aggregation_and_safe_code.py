

# Exercises: Design, aggregation and safe code

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 1.

# Depending a little bit on how many reviews are expected, but my first intuition is to have the reviews embedded. They seem to belong with the book and will be shown
# with that book. For the members I say reference: That one will contain personal data, so its good to have that in ONE safe space. It also seems like there is no
# real need for having the members tightly connected to a particular book. I'd prefer a separate collection for "loans", cause that will grow over time. And it might be 
# prudent to keep some history for statistics.

# 2.

# One advantage is that the copy will keep its data correct for that point in time even if the data changes on the product itself (price will change over time for example).
# One disadvantage is that, depending on how the database is used, the copys needs updating everywhere they exist if they should follow any changes in the product.

# 3.
'''
db.create_collection("newsletter_signups", validator={"$jsonSchema": {
"required": ["email", "source"],
"properties": {"email": {"bsonType": "string"},
    "source": {
        "enum": ["web", "store"],
        "description": "source must be either web or store"}}}})
'''

'''
# Working:
db.newsletter_signups.insert_one({"email": "test@test.com", "source": "web"})
# Fails on source:
db.newsletter_signups.insert_one({"email": "test2@test2.com", "source": "word on the street"})
'''

# 4.
'''
cities = (db.customers.aggregate([
    {"$group": {"_id": "$city",
                 "city": {"$sum": 1}}},
                 {"$sort": {"city": -1}}
]))

for city in cities:
    print(city)
'''
# 5.

'''
categories = (db.products.aggregate([
    {"$group": {"_id": "$category",
                "max": {"$max": "$price"}, 
                "min": {"$min": "$price"}}}
]))

for category in categories:
    print(category)
'''

# 6.
'''
customers = db.orders.aggregate([
    {"$group": {"_id": "$customer_id",
                "orders": {"$sum": 1}}},
    {"$match": {"orders" :{"$gte": 2}}},
    {"$sort": {"orders": -1}}
])

for customer in customers:
    print(customer)
'''

# 7.
'''
orders = db.orders.aggregate([
    {"$project": {"items": {"$size": "$items"}}}
])

for order in orders:
    print(order)
'''

# 8.
'''
categories = (db.orders.aggregate([
    {"$match": {"status" :{"$ne": "cancelled"}}},
    {"$unwind": "$items"},
    {"$lookup": {"from": "products", 
                 "localField": "items.product_id", 
                 "foreignField": "_id", 
                 "as": "product"}},
    {"$group": {"_id": "$product.category",
                    "units": {"$sum": "$items.quantity"}}}
]))

for category in categories:
    print(category)
'''

# 9.
'''
statuses = (db.orders.aggregate([
    {"$unwind": "$items"},
    {"$project": {"status": 1, "line_total": {"$multiply": ["$items.unit_price", "$items.quantity"]}}},
    {"$group": {"_id": "$status",
                    "total": {"$sum": "$line_total"}}}
]))

for status in statuses:
    print(status)
'''

# 10.
'''
tags = (db.products.aggregate([
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]))

for tag in tags:
    print(tag)
'''