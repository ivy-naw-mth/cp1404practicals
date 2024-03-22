MINIMUM_LENGTH = 4
def main():
    """Password to stars program"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)

def get_password(minimum_length):
    """Getting password with minimum length"""
    password = input(f"Enter the password which at least has {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter the password which at least has {minimum_length} characters: ")
    return password

def print_asterisks(sequence):
    """Print * 'equals to' Length of password"""
    print('*' * len(sequence))

main()