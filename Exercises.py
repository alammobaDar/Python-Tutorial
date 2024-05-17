# password checker

import re
def is_valid(password):
    if len(password) < 8:
        print("Password must have more than 8 characters")
        return False
    if not re.search("[a-z]", password):
        print("Password must have an lowercase letter")
        return False
    if not re.search("[A-Z]", password):
        print("Password must have an Uppercase letter")
        return False
    if not re.search("[0-9]", password):
        print("Password must have a number on it")
        return False
    if not re.search("[!@#$%^&*()_+={}:;""''<>,.?/]", password):
        print("Password must have a special character")
        return False
    return True

password = input("Enter a pasword: ")

if is_valid(password):
    print("Your password is valid!")
else:
    print("Your password is not valid!")
