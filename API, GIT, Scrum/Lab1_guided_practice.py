



# Lab 1: Guided practice


import requests

def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The request took too long")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server")
    except requests.exceptions.HTTPError as error:
        print(f"The server said no: {error.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("The answer was not JSON")
    except requests.exceptions.RequestException as error:
        print(f"Someting else went wrong: {type(error).__name__}")
    return None


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