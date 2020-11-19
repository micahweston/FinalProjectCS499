# Stephen Weston
# 11/1/2020
# User Management System

# import databases, and database connections
import sqlite3
conn = sqlite3.connect("user_management.db")
cursor = conn.cursor()

from crud import Crud

class Customer:
    """
    Customer class designed to do all things customer. Methods present are existing_customer, new_customer, 
    search_customer, add_customer, view_customer, delete_customer, update_customer. This class will be linked
    to our database CRUD class.
        
    """
    def __init__(self):
        """This is our Crud class initiation"""
        self.crud_proc = Crud()

    def existing_customer(self):
        """
        Existing customer process. Will be linked to search_customer, view_customer, edit_customer, 
        and delete_customer methods.
        """
        print("========================================================")
        print("================= Existing Customers ===================\n")
        print("1. View Customer")
        print("2. Update Customer")
        print("3. Delete Customer\n")
        user_input = input("Please select your option: ")
        user_input = int(user_input)
        if user_input == 1:
            self.view_customer()
        elif user_input == 2:
            self.edit_customer()
        elif user_input == 3:
            self.delete_customer()
        else:
            print("Not a valid input")


    def new_customer(self): 
        """
        New customer process. Will be linked to add_customer method.
        """
        print("New Customer Test")
        pass

    def search_customer(self):
        """ Process search feature in database. Will be based off of id or last name. """
        pass

    def add_customer(self):
        """ Add customer to database"""
        pass

    # View Customer info from database. Using CRUD file.
    def view_customer(self):
        """ 
        View customer from database, gives option to view newest customer or view all customers. 
        """
        print("========================================================")
        print("================= Read Customer Info ===================")
        print("1. View newest customer:")
        print("2. View all customers:\n")
        # Collect user selection
        user_input = input("How many customers would you like to see? ")
        user_input = int(user_input)
        self.crud_proc.read(user_input)
        user_input = input("Would you like to view another customer? (Y/N)")
        if user_input.lower() == 'y':
            self.view_customer()
        elif user_input.lower() == 'n':
            return
        else:
            print("Not a valid input.")

    def delete_customer(self):
        """ Delete customer method will link to delete feature in Crud class"""
        print("Not built yet")

    def edit_customer(self):
        """ Edit customer method will link to update feature in Crud class"""
        print("Not built yet")