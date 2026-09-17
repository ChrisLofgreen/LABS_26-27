# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products. check
# 2. Print the name of every product that is in stock. check
# 3. Calculate the total value of all products in stock. check
#    The value of a product is price * stock.
# 4. Print the total value. check
# 5. Keep track of which in-stock product has the highest price check
#    without using max(), and print its name. check


# Write your solution below:
'''
product_value = 0
total_value = 0
high_price = 0
high_price_name = ""

for product in products:
    if product["stock"] > 0:
        print(product["name"])
        product_value = product["stock"] * product["price"]
        total_value = total_value + product_value

        if product["price"] > high_price:
            high_price = product["price"]
            high_price_name = product["name"]


print(total_value)
print(high_price_name)
'''
# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores check
# - calculates and returns the average score check
#
# Create another function called create_result that:
# - receives a list of scores check
# - uses calculate_average() check
# - returns "PASS" if the average is 70 or higher check
# - otherwise returns "FAIL" check
#
# Call create_result() using the scores above. check
# Print both the average score and the final result. check


# Write your solution below:
'''
def calculate_avarage(list_of_scores):
    avarage = sum(list_of_scores) / len(list_of_scores)
    return avarage

def create_result(list_of_scores):
    if calculate_avarage(list_of_scores) >= 70:
        return "PASS"
    return "FAIL"

result = create_result(scores)

print(f"Avarage score: {calculate_avarage(scores)}\nResult: {result}")
'''

# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter check
# - receives any number of product prices using *args check
# - receives optional settings using **kwargs check
# - calculates the subtotal of all product prices check
# - applies the discount percentage if "discount" exists check
# - adds shipping if "shipping" exists check
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:
'''
def calculate_order(name, price_list, order_settings, *args , **kwargs):
    customer = name
    prices = price_list
    settings = order_settings
    subtotal = 0
    final_total = 0

    for price in args:
        prices.append(price)

    for key, value in kwargs:
        settings[key] = value

    subtotal = sum(prices)
    final_total = subtotal

    if "discount" in settings:
        final_total = final_total * (1 - (settings["discount"] / 100))

    if "shipping" in settings:
        final_total = final_total + settings["shipping"]


    output = {"customer" : customer, 
              "subtotal": subtotal, 
              "final_total": final_total, 
              "settings": settings}

    return(output)


order = calculate_order("Anna", product_prices, order_settings)

print(order)
'''

# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
'''
# 1.
stripped = [player["name"].strip() for player in players]
lowered = [player.lower() for player in stripped]

# 2.

above_80 = [player["name"] for player in players if player["score"] >= 80 and player["active"] == True]

# 3.

sorted_list = sorted(players,
                     key=lambda player:player["score"], 
                     reverse=True)

for player in sorted_list:
    player["name"] = player["name"].strip()
    player["name"] = player["name"].lower()

print(sorted_list)

# 4.

for index, player in enumerate(sorted_list, start=1):
    print(f"{index}. {player["name"]} - {player["score"]}")

# 5.

names = [player["name"] for player in sorted_list]

scores = [player["score"] for player in sorted_list]

names_scores = {}

for name, score in zip(names, scores):
    names_scores[name] = score

'''