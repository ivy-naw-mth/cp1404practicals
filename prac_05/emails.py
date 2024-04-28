"""
Word Occurrences
Estimate: 30 minutes
Actual: 35 minutes
"""

def main():
    email_to_name = {}
    email = validate_email()
    user_name = name_processing(email)
    while email != "":
        choice = input(f"Is your name {user_name}? (Y/n) ").upper()
        if choice == "Y":
            email_to_name[email] = user_name
        else:
            modified_name = input("Name: ")
            email_to_name[email] = modified_name
        email = validate_email()
        user_name = name_processing(email)

    for email in email_to_name:
        print(f"{email_to_name[email]} ({email})")

def name_processing(email):
    """Identifying user email and their username"""
    name = email.split('@')[0]
    name_parts = name.split('.')
    name_parts = [part.title() for part in name_parts]
    name = ' '.join(name_parts)
    return name

def validate_email():
    """Checking the email is valid or not"""
    email = input("Email:")
    if email == "":
        return email
    while '@' not in email:
        print("This is not a valid email,please try again!")
        email = input("Email:")
    return email

main()