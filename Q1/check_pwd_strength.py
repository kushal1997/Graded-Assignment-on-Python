

def check_password_strength(pwd):
    if len(pwd) >= 8:
        print("1) Minimum password length criteria achived")
    else:
        print("1) Password must be 8 chars long")
        return False
    
    check_uppercase_letters = False
    check_smallcase_letters = False

    check_numbers = False

    check_special_chars = False

    for ch in pwd:
        if ch >= 'A' and ch <= 'Z':
            check_uppercase_letters = True
        elif ch >= 'a' and ch <= 'z':
            check_smallcase_letters = True
        elif ch >= '0' and ch <= '9':
            check_numbers = True
        else:
            check_special_chars = True
    
    if check_uppercase_letters:
        print("2) Contains uppercase letter")
    else:
        print("2) Missing uppercase letter")
    
    if check_smallcase_letters:
        print("3) Contains lowercase letter")
    else:
        print("3) Missing lowercase letter")

    if check_numbers:
        print("4) Contains digit")
    else:
        print("4) Missing digits")
    
    if check_special_chars:
        print("5) Contains special characters")
    else:
        print("5) Missing special character")
    
    return check_uppercase_letters and check_smallcase_letters and check_numbers and check_special_chars



password = input("Enter your password : ")
print("\n Checking password trength ... \n")


if check_password_strength(password):
    print("\n Your password is strong")
else:
    print('\n Your password is weak . Please imrove it')