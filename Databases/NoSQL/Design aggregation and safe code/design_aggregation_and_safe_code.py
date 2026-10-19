

# Exercises: Design, aggregation and safe code

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 1.

# Depending a little bit on how many reviews are expected, my first intuition is to have the reviews embedded. They seem to belong with the book and will be shown
# with that book. For the members I'd say reference: That collection will contain personal data, so its good to have that in ONE safe space. It also seems like there is no
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

# 11.
'''
import json
from pprint import pprint

def find_orders(request_text):
    data = json.loads(request_text)
    return list(db.orders.find({"status": data["status"]}))

#pprint(find_orders('{"status": "new"}'))

#pprint(find_orders('{"status": {"$ne": "x"}}'))
'''

# The function is unsafe since it allows for injection. "not equal to x" is the injection here, 
# which return all of the orders in the database, not great. The json.loads() automaticly converts from JSON to Python which makes
# it an injection risk. In this case a JSON object gets converted to a Python dictionary, So the funtion allows for a nested dict with any symbols.

# Below is my solution which can handle the same inputs but differentiate between a regular input and an injection.
# First of all the input data is constrained to a Python-string, and it is in this state all the checking is handled.
# Then there is a matching process which checks that the pattern is what we expect, "status" and then ":", blank spaces are allowed in
# certain places but nothing else. The value-part of the string is only allowed to be made of a-z and/or A-Z (no "$" for example). \A and \Z in the beginning and end
# of the pattern futher makes sure that it only allows for one entire string (no nested values). (overkill in this example but it doesnt affect functionality)
# The database query is then rebuilt whith the value part of the string to make a new dict. The rebuild is constrined so that it can only
# query the "status" field (overkill since we already checked for "status", or an extra layer of security, no extra lines of code).


from pprint import pprint
import re

def find_orders(request_text):
    data = str(request_text)

    pattern = r'\A\{\s*"status"\s*:\s*"[a-zA-Z]*"\s*\}\Z'
    valid = bool(re.match(pattern, data))

    if valid:
        data = data[11:-1].strip()
        data = data.replace("\"", "")
        data = {"status": data}
        return list(db.orders.find(data))
    else:
        return "Invalid input"

    
# pprint(find_orders('{"status": "new"}'))

# pprint(find_orders('{"status": {"$ne": "x"}}'))


# 12.

'''
from pprint import pprint

def products_under(text):
    try:
        data = float(text)
        return list(db.products.find({"price": {"$lt": data}}, {"name": 1, "price": 1, "_id": 0}))

    except ValueError:
        print ("Please enter a number")
        data = []
        return data



pprint(products_under('{"$gt"}: 0'))
pprint(products_under("abc"))
pprint(products_under("300"))
'''

# 13.
'''
import pymongo.errors

client2 = MongoClient("mongodb://localhost:27018/", serverSelectionTimeoutMS=2000)
db = client2["webshop"]

try:
    count = db.products.count_documents({})
    print(count)

except pymongo.errors.ServerSelectionTimeoutError:
    print("Server selection timed out, no server found")


client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
db = client["webshop"]

try:
    count = db.products.count_documents({})
    print(count)

except pymongo.errors.ServerSelectionTimeoutError:
    print("Server selection timed out, no server found")
'''

# 14.

# first_name, last_name, email, city is personal data. The orders are personal-data to the extent that
# they can be connected to the person, so that can be anonymized. That is why it is good to not
# have the personal data in the order collection when a customer asks to be deleted. The order data
# needs to be there for the books but with this setup the personal data can be removed without affecting the
# order data.

# Regarding the copying of email and city:
# The copying of the customers email and city onto every order makes a "delete me" job much harder.
# All of a sudden all orders made by the customer needs to be interacted with, and any misstake means
# that the obligations by law have not been met.
# The other argument against this is that personal data is sensitive information and should be kept
# where it is easy to manage and control access. This approach make that harder. 
# Therefore "faster reading" is not a strong enough reason to freeze that data onto those orders,
# it's better to reference in this case.