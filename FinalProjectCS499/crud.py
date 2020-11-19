# Stephen Weston
# 11/1/2020
# User Management System

# import databases, and database connections
import pandas as pd
import sqlite3
conn = sqlite3.connect("user_management.db")
cursor = conn.cursor()

class Crud:
    """
    This is our database class. This class is designed to allow the user to create, read, update, 
    and delete user information from the database. This is linked directly to the customer.py module.
    """
    def create(self, id, name, email, address, employer):
        """ Update customer information in database. """
        cursor.execute('''INSERT INTO customers VALUES(self.id, self.name, self.email, self.address, self.employer)''')
        conn.commit()

    def read(self, user_input):
        """ Read customer information in database. """
        self.user_input = user_input
        # Test user input to make sure it is valid
        if self.user_input == 1:
            df = pd.read_sql_query(""" SELECT * FROM customers;""", conn)
            return print(df.tail(1))
        elif self.user_input == 2:
            df = pd.read_sql_query(""" SELECT * FROM customers;""", conn)
            return print(df)
        else:
            print("Invalid selection: Please select the number that corresponds to \nyour selection")
            return
        

    def update(self):
        """ Update customer information in database. """
        pass

    def delete(self):
        """ Delete customer information in database. """
        pass