

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
