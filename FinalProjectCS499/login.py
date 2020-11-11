# Stephen Weston
# 11/1/2020
# User Management System

# import csv library
import csv

#implementation of login class to use for login verification
class Login: 
    # user_find method to verify the user is in txt file.
    def user_find(self):
        """Requests User Id and verifies it exists in users.txt 
            Returns the userid if found, else returns None """
        with open("users.txt") as file:
            file_reader = csv.reader(file)
            count = 2
            while count >= 0:
                file.seek(0)  # Repositions read pointer to start of file
                user = input("Please enter your username: ")
                user_found = None
                for row in file_reader:
                    if row[0].lower() == user.lower():
                        count = -1
                        user_found = row
                        break
 
                if user_found:       #Test for valid userId being detected
                    file.close()  # closes file on exit from while loop
                    if self.pass_check(user_found):
                        return user_found[0]
                    else:
                        return None                        
                else:
                    print("Invalid Username")
                    print(f"You have {count} attempts to login left.")
                    count -= 1 
            file.close()  # closes file on exit from while loop
            return None                                    

    
    def pass_check(self, row):
        """ Checks for valid password entry.  If entry is valid, 
            returns True, else False"""
        count = 3
        while count > 0:
            password = input("Please enter your password: ")
            if str(row[1]).strip() == password.strip():
                return True
        
            print("Invalid Password")
            count -= 1
            print(f"You have {count} attempts to login left.")
        return False
