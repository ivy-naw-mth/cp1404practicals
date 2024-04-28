try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Questions
---------
1. When will a ValueError occur?
Answer: ValueError will occur when we type something else for the numerators and denominators 
and the input(s) is/are not numbers.
2. When will a ZeroDivisionError occur?
Answer: When we type the denominator input as 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Adding while loop to validate the number can prevent/avoid the zero division error.
"""
