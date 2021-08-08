# Stephen Weston
# 11/1/2020
# User Management System

# import additional files
from login import Login
from customer import Customer
import pandas as pd

# import databases, and database connections
import sqlite3
conn = sqlite3.connect("user_management.db")
cursor = conn.cursor()

# Welcome screen
def welcome():
    """ Welcome screen for program """
    print("========================================================")
    print('======================== Wecome ========================')
    print("========================================================")
    print('================= User Management System ===============')
    print("========================================================\n")

# Login function
def start():
    """Start function designed to implement the login screen."""
    # Function to initiate login operations
    log_req = input("Login to your account (Y/N) ")
    if log_req.lower() == 'y':  # This ensures that if the user types 
                               # upper or lower case, it is detected
        log_proc = Login()
        if log_proc.user_find():
            print('\nWelcome to the System\n')
        else:
            print('Please contact your administrator to setup your account')
    else:
        print ('Goodbye')

# Menu to be seen after proper login
def menu():
    """Menu to make selection"""
    print("========================================================")
    print('======================== Menu ==========================')
    print("========================================================\n")
    print('1. New customer: ')
    print('2. Existing customer: ')
    print('3. Exit\n')
    
    customer_proc = Customer()
    user_input = input('Please make your selection using a numerical value: ')
    user_input = int(user_input)
    # Checking to see what user input is, and make send to correct method.
    if user_input == 1:
        customer_proc.new_customer()
    elif user_input == 2:
        customer_proc.existing_customer()
    elif user_input == 3:
        return
    else:
        print('Invalid choice, please select the number corresponding to the selection:')
        menu()
    menu()

# Exit message
def exit_program():
    """ Thank you message to exit program """
    print('===============================================')
    print("Thank you for using the User Management System!")
    print('===============================================')
    return

# Initialize main program
def program():
    """Program basic flow."""
    welcome()
    start()
    menu()
    exit_program()

# initial load of customers to database 
customers = [(101, 'Joe Frank', 'joe@ymail.com', '1234 Yorktown Ave. New York, 10001', 'Vivint'), 
(102, 'Nancy Jull', 'nancy@ymail.com', '1254 Something Ave. New York, 10001', 'Google'), 
(103, 'George Williams', 'george@ymail.com', '12554 York Ave. New York, 10001', 'Yahoo'), 
(104, 'Billie Elish', 'billie@ymail.com', '1232 Penn Ave. New York, 10001', 'Apple'),
(105, 'Sam York', 'sam@ymail.com', '15553 Penn Ave. New York, 10001', 'Apple')] 

# Start Program
program()

