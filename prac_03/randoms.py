# Function testing exercise from practical
"""
#given example code
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""
# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# Answer: For line 1, the smallest number we can get is 5 and the largest is 20.

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# Answer: For line 2, the smallest number we can get is 3 and largest is 9.

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# Answer: In line 3, the smallest number we can get is 2.5 and the largest is 5.5.


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
print(random.randint(1,100))