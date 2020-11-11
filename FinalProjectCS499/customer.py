# Stephen Weston
# 11/1/2020
# User Management System

# import databases, and database connections
import sqlite3
conn = sqlite3.connect("user_management.db")
cursor = conn.cursor()

class Customer:
    # intialize Customer class
    def __init__(self):
        self.crud_proc = Crud()

    def existing_customer(self):
        print("Existing Customer Test")
        self.view_customer()

    def new_customer(self):
        print("New Customer Test")
        pass

    def search_customer(self):
        pass

    def add_customer(self):
        pass

    # View Customer info from database. Using CRUD file.
    def view_customer(self):
        print("========================================================")
        print("================= Read Customer Info ===================")
        print("1. View newest customer:")
        print("2. View all customers:")
        # Collect user selection
        user_input = input("How many customers would you like to see? ")
        user_input = int(user_input)
        self.crud_proc.read(user_input)

    def delete_customer(self):
        pass

    def save_customer(self):
        pass

    def edit_customer(self):
        pass

# import databases, and database connections
import sqlite3
conn = sqlite3.connect("user_management.db")
cursor = conn.cursor()

class Crud:
    def __init__(self):
        self.customer_proc = Customer()

    # Update customer information in database
    def create(self, id, name, email, address, employer):
        cursor.execute('''INSERT INTO customers VALUES(self.id, self.name, self.email, self.address, self.employer)''')
        conn.commit()

    # Read customer information in database
    def read(self, user_input):
        self.user_input = user_input
        # Test user input to make sure it is valid
        if self.user_input == 1:
            cursor.execute("SELECT * FROM customers").fetchone()
        elif self.user_input == 2:
            cursor.execute("SELECT * FROM customers").fetchall()
        else:
            print("Invalid selection: Please select the number that corresponds to \nyour selection")
            self.customer_proc.view_customer()
    
    # Update customer information in database
    def update(self):
        pass

    # Delete customer information in database
    def delete(self):
        pass
