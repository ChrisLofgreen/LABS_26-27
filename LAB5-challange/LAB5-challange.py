

products = [
    {"name": "Gibson Les Paul Standard",
     "colour": "Cherry Sunburst",
     "price": 25000,
     "category": "Guitar"},
    {"name": "Gibson Les Paul Classic",
     "colour": "Honeyburst",
     "price": 18000,
     "category": "Guitar"},
     {"name": "Gibson SG Standard",
      "colour": "Red",
      "price": 15000,
      "category": "Guitar"},
      {"name": "Fender Stratocaster",
       "colour": "Red",
       "price": 17000,
       "category": "Guitar"},
       {"name": "Vigier Excalibur Surfreter Special",
       "colour": "Multi-coloured",
       "price": 40000,
       "category": "Guitar"},
       {"name": "Vox AC30",
       "colour": "Black",
       "price": 25000,
       "category": "Amplifier"},
       {"name": "Marshall 2555 SL",
        "colour": "Black",
        "price": 27000,
        "category": "Amplifier"},
        {"name": "Marshall Plexi",
         "colour": "Black",
         "price": 30000,
         "category": "Amplifier"},
]


customers = [
    {"customer_id": 1,
     "customer_name": "Guthrie Govan",
     "customer_email": "guthrie@govan.com"},
     {"customer_id": 2,
      "customer_name": "Mark Knopfler",
      "customer_email": "mark@dire-straits.com"},
      {"customer_id": 3,
       "customer_name": "Ron Thal",
       "customer_email": "ron@thal.com"},
       {"customer_id": 4,
        "customer_name": "Brian May",
        "customer_email": "brian@queen.com"},
        {"customer_id": 5,
         "customer_name": "Soul Hudson",
         "customer_email": "slash@gnr.com"}
]


last_order_id = 0

def order_counter():
    return last_order_id + 1

def calculate_subtotal(*prices):
    return sum(prices)

def order_configuration(**order_options):
    options = {key: value for key, value in order_options.items() 
               if value != None}

    return options


def order_creator(customer_id, *ordered_products, **options,):
    order_id = order_counter()
    
    products_on_order = [product for product in ordered_products]

    order_options = {key: value for key, value in options.items()}

    return order_id, customer_id, products_on_order, order_options




print(order_creator(3, "Marshall 2555 SL", "Marshall Plexi", priority=True, discount=20))

last_order_id = order_counter()

print(order_creator(4, "Marshall 2555 SL", "Marshall Plexi", priority=True, discount=20))

last_order_id = order_counter()

print(order_configuration(priority=True, discount=20, test=None))

