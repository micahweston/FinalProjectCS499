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
        print("================= Existing Customers ===================")
        print("========================================================\n")
        print("1. View Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print('4. Exit\n')
        user_input = input("Please select your option: ")
        user_input = int(user_input)
        if user_input == 1:
            self.view_customer()
        elif user_input == 2:
            self.edit_customer()
        elif user_input == 3:
            self.delete_customer()
        elif user_input == 4:
            return
        else:
            print("Not a valid input")


    def new_customer(self): 
        """
        New customer process. Will be linked to add_customer method.
        """
        print("========================================================")
        print("==================== New Customers =====================")
        print("========================================================")
        self.add_customer()

    def search_customer(self):
        """ Process search feature in database. Will be based off of id or last name. """
        pass

    def add_customer(self):
        """ Add customer to database"""
        # create variables needed to save customer info to add to database.
        cust_id, cust_name, cust_email, cust_address, cust_employeer = '', '', '', '', ''

        # Get customer information
        cust_id = input("Please enter new ID (cannot be used already): ")
        cust_name = input("Please enter customer name: ")
        cust_email = input("Pleae enter customer email: ")
        cust_address = input("Please enter customer address: ")
        cust_employeer = input("Please enter customer employeer: ")

        # Verify information given
        print(f"Please verify that customer information is valid? \n\nNew ID: {cust_id}")
        print(f"Custmer Name: {cust_name} \nCustomer Email: {cust_email} \nCustomer Address: {cust_address} \nCustomer's Employeer: {cust_employeer}")

        # Ask if information is correct. Based on answer will run add_customer() again.
        user_input = input("\nIs the information correct? (Y/N)")
        if user_input.lower() == 'y':        
            self.crud_proc.create(cust_id, cust_name, cust_email, cust_address, cust_employeer)
        else:
            new_input = input("Would you like to enter the information again? (Y/N)")
            if new_input.lower() == 'y':
                self.add_customer()
            else:
                print("\nPlease try again at a later time!")
                return

    # View Customer info from database. Using CRUD file.
    def view_customer(self):
        """ 
        View customer from database, gives option to view newest customer or view all customers. 
        """
        print("========================================================")
        print("================= Read Customer Info ===================")
        print("1. View newest customer:")
        print("2. View all customers:")
        print('3. Exit\n')

        # Collect user selection
        user_input = input("Please make a selection: ")
        print("")
        user_input = int(user_input)
        if user_input == 1 or user_input == 2:
            self.crud_proc.read(user_input)
        elif user_input == 3:
            return
        else:
            print("Not a valid input.")
            self.view_customer()
        
        # After return from crud.py we will ask if customer wants to view more customers.
        user_input = input("\nWould you like to view another customer? (Y/N) ")
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