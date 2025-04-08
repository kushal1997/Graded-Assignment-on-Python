
# function to check strenght of password
def check_password_strength(pwd):
    # first check for minimum password length
    if len(pwd) >= 8:
        print("1) Minimum password length criteria achived")
    else:
        print("1) Password must be 8 chars long")
        return False # early EXIT if condition is not met
    
    # checks for rest requirement
    check_uppercase_letters = check_smallcase_letters =  check_numbers = check_special_chars = False

    # looping characters of password
    for char in pwd:
        if char.isupper():
            check_uppercase_letters = True
        elif char.islower():
            check_smallcase_letters = True
        elif char.isdigit():
            check_numbers = True
        elif not char.isalnum(): # its NOT as special characters are not alpha numeric
            check_special_chars = True

    # print status of each requirements
    if check_uppercase_letters:
        print("2) Contains uppercase letter")
    else:
        print("\n 2) Missing uppercase letter")
    
    if check_smallcase_letters:
        print("3) Contains lowercase letter")
    else:
        print("\n 3) Missing lowercase letter")

    if check_numbers:
        print("4) Contains digit")
    else:
        print("\n 4) Missing digits")
    
    if check_special_chars:
        print("5) Contains special characters")
    else:
        print("\n 5) Missing special character")
    
    # return TRUE only if all checks are passed
    return check_uppercase_letters and check_smallcase_letters and check_numbers and check_special_chars


# takes user input
password = input("Enter your password : ")
print("\n Checking password trength ... \n")


# final answer based on function's return
if check_password_strength(password):
    print("\n Your password is strong")
else:
    print('\n Your password is weak . Please imrove it')