"""
Password Validator: 
Write a function that checks a password's validity based 
on criteria like minimum length, containing 
uppercase/lowercase letters, and a special character. 
The function should return True if valid, False otherwise.
"""

import re

def password_validator(password):
    # Check if password length is at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if password contains uppercase and lowercase letters
    if not re.search("[A-Z]", password) or not re.search("[a-z]", password):
        return False
    
    # Check if password contains at least one digit
    if not re.search("[0-9]", password):
        return False
    
    # Check if password contains at least one special character
    if not re.search("[!@#$%^&*()-_+=]", password):
        return False
    
    # If all criteria are met, return True
    return True

# Test the function
password = input("Enter your password: ")
if password_validator(password):
    print("Valid password!")
else:
    print("Invalid password!")
