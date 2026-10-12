import sqlite3


def connect():
    conn = sqlite3.connect("Databases/Python_and_personal_data/webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    while True:
        try:
            price = float(input("Price: "))
            break
        except ValueError:
            print("\nOnly numbers in price, please try again\n")
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")


def change_stock(conn):
    prod_id = input("Product id: ")
    new_stock = int(input("Type new stock value: "))
    conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?",
        (new_stock, prod_id))
    conn.commit()
    print("New stock value saved!")


def show_receipt(conn):
    order_id = int(input("Order id: "))
    cursor = conn.execute(
        """
        SELECT p.name, oi.quantity, p.price, p.price * oi.quantity line_total 
        FROM order_items oi 
        JOIN products p ON oi.product_id = p.product_id 
        WHERE order_id = ?""",
        (order_id,))
    for name, quant, price, line_total in cursor.fetchall():
        print(f"{name:<16}|Quantity: {quant}|Price: {price:.0f}|Line total: {line_total}|")


def best_selling_products(conn):
    cursor = conn.execute(
        """
        SELECT p.name, SUM(oi.quantity) AS quant_count
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY p.name
        ORDER BY quant_count DESC
        LIMIT 3
        """)
    for name, quant in cursor.fetchall():
        print(f"{name:<16}| Items Sold: {quant}")
    

def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product 4) Change stock 5) Show receipt 6) Top 3 best-selling products 0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_receipt(conn)
        elif choice == "6":
            best_selling_products(conn)
        elif choice == "0":
            break
    conn.close()


main()
