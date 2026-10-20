



# Lab 1: Guided practice


from api_client import get_json
import requests


# 1.
'''
products = get_json("https://fakestoreapi.com/products")
sorted_products = sorted(products, key=lambda x: x["price"])
for product in sorted_products:
    print(f"{product["price"]:<7,.2f}- {product["title"]}")
'''

# 2.
'''
categories = get_json("https://fakestoreapi.com/products/categories")
print(categories)

user_input = str(input("Type a category:")).strip()

products = get_json(f"https://fakestoreapi.com/products/category/{user_input}")

if len(products) > 0:
    min = min(products, key=lambda x:x["price"])
    print("cheapest product id:", min["id"])
    print("number of products:", len(products))
else:
    print("That category doesnt seem to exist")
'''

# 3.

# check

# 4.
'''
new_product = {
    "title": "Superhat",
    "price": 89.99,
    "description": "Hat includes rabbit!",
    "image": "",
    "category": "men's clothing",
}

response = requests.post("https://fakestoreapi.com/products", json=new_product, timeout=200)
print(response.status_code)
print(response.json())


response = requests.patch("https://fakestoreapi.com/products/10", json={"price": 99.99}, timeout=200)
print(response.status_code)
print(response.json())
'''

# 5.
'''
response = get_json("fakestoreapi.com/products")

response = get_json("https://fakestoreapi.com/products", timeout=0.001)

response = get_json("https://this_is_probalbly_not_a_valid_url_abcdefg.nu")
'''

