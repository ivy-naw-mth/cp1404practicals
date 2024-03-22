is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished=True
        print("This is valid!!!!")
        #Exit the loop if a valid integer is entered
    except ValueError: #Handle ValueError Exception
     print("Please enter a valid integer.")
print("Valid result is:", result)