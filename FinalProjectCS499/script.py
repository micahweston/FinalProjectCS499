# Stephen Weston
# 11/1/2020
# User Management System

# import additional files
from hash_map import HashMap
from login import Login
from customer import Customer



def welcome():
    """ Welcome screen for program """
    print('============================================')
    print('================== Wecome ==================')
    print('============================================')
    print('=========== User Management System =========')
    print('============================================')


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

def menu():
    """Menu to make selection"""
    print('============================================')
    print('================== Menu ====================')
    print('============================================\n')
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
        exit_program()
    else:
        print('Invalid choice, please select the number corresponding to the selection:')
        menu()
    return


def exit_program():
    """ Thank you message to exit program """
    print('===============================================')
    print("Thank you for using the User Management System!")
    print('===============================================')
    return

def program():
    """Program basic flow."""
    welcome()
    start()
    menu()


program()

