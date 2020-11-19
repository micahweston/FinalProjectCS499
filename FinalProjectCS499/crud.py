# Stephen Weston
# 11/1/2020
# User Management System

# import Customer Class from customer.py


# import databases, and database connections
import sqlite3
conn = sqlite3.connect("user_management.db")
cursor = conn.cursor()

class Crud:
    """
    This is our database class. This class is designed to allow the user to create, read, update, 
    and delete user information from the database. This is linked directly to the customer.py module.
    """
    def __init__(self):
        pass

    def create(self, id, name, email, address, employer):
        """ Update customer information in database. """
        cursor.execute('''INSERT INTO customers VALUES(self.id, self.name, self.email, self.address, self.employer)''')
        conn.commit()

    def read(self, user_input):
        """ Read customer information in database. """
        self.user_input = user_input
        # Test user input to make sure it is valid
        if self.user_input == 1:
            customer = cursor.execute("SELECT * FROM customers").fetchone()
        elif self.user_input == 2:
            customer = cursor.execute("SELECT * FROM customers").fetchall()
        else:
            print("Invalid selection: Please select the number that corresponds to \nyour selection")
            return
        return print(customer)

    def update(self):
        """ Update customer information in database. """
        pass

    def delete(self):
        """ Delete customer information in database. """
        pass