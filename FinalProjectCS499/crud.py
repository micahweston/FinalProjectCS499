# Stephen Weston
# 11/1/2020
# User Management System

# import Customer Class from customer.py


# import databases, and database connections
import sqlite3
conn = sqlite3.connect("user_management.db")
cursor = conn.cursor()

class Crud:
    def __init__(self):
        from customer import Customer
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
