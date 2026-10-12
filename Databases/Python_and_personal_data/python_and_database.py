

# Exercises: Python and personal data

# 1.
'''
import sqlite3

conn = sqlite3.connect("Databases/Python_and_personal_data/webshop.db")
cursor = conn.cursor()

cursor.execute("SELECT first_name, last_name, city FROM customers")
for first_name, last_name, city in cursor.fetchall():
    print(f"{first_name} {last_name} ({city})")
    
conn.close()
'''

# 2.
'''
import sqlite3

conn = sqlite3.connect("Databases/Python_and_personal_data/webshop.db")
cursor = conn.cursor()

maxprice = input("Type your max price: ")

cursor.execute(
    "SELECT name, price FROM products WHERE price < ?", (maxprice,))

for name, price in cursor.fetchall():
    print(f"{name:<20} {price:.0f} kr")

conn.close()
'''

# 3.
'''
import sqlite3

conn = sqlite3.connect("Databases/Python_and_personal_data/webshop.db")
cursor = conn.cursor()

user_cat = input("Type a category:")

cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?", (user_cat,))

user_cat_num, = cursor.fetchone()

print(user_cat_num)
'''

# 4.
