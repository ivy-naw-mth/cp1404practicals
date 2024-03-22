MINIMUM_LENGTH = 2
MAXIMUM_LENGTH = 6
REQUIRED_SPECIAL_CHARACTERS = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MINIMUM_LENGTH, "and", MAXIMUM_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if REQUIRED_SPECIAL_CHARACTERS:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")

def is_valid_password(password):
    """Determining the validation of provided password."""
    # Check the password length is wrong or not, if not return False
    if not MINIMUM_LENGTH < len(password) < MAXIMUM_LENGTH:
        print(f"Your password must be between 2 and 6 characters")
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # Count each kind of character in the passwords
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        pass

    # If any of the 'normal' counts are zero, return False
    if count_lower < 1 or count_digit < 1 or count_upper < 1:
       return False
    # If special characters are required, then check the count of those characters
    # and return False if it's zero
    if REQUIRED_SPECIAL_CHARACTERS:
        for char in password:
            if char in SPECIAL_CHARACTERS:
                count_special += 1
        if count_special < 1:
            return False
    # The password must be valid if the code runs smoothly till here.
    return True

main()
