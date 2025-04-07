

def check_password_strength(pwd):
    if len(pwd) >= 8:
        print("1) Minimum password length criteria achived")


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


        if check_uppercase_letters and check_smallcase_letters:
            print("2) Contains both uppercase and lowercase letters")

            if check_numbers:
                print('3) Contains at least one digit (0-9)')

                if check_special_chars:
                    print('4) Contains at least one special character (e.g., !, @, #, $, %)')
                    
                    print("")
                    return print("Password passed all criteria")
                else:
                    print("")
                    print("Password stength check failed !!! ")

                    print("4) Must have atleastat least one special character (e.g., !, @, #, $, %)")

            else:
                print("")
                print("Password stength check failed !!! ")
                return print("3) Must have atleast one digit (0-9)")
        else:
            print("")
            print("Password stength check failed !!! ")
            return print("2) Must have atleast one upper and lower case letters")
    else:
        print("")
        print("Password stength check failed !!! ")
        return print("1) Password should be of minimum 8 characters")

password = input("Enter your password : ")
print("Checking password trength ...")
print("")

check_password_strength(password)