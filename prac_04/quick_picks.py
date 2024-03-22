import random

MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45
NUMBERS_PER_QUICK_PICK = 6

number_pick = int(input("How many quick picks? "))
for i in range(number_pick):
    number_list = []
    for j in range(NUMBERS_PER_QUICK_PICK):
        number = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
        while number in number_list:
            number = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
        number_list.append(number)
    number_list.sort()
    print(" ".join("{:2}".format(number) for number in number_list))
