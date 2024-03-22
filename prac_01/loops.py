#example
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10 from 0 to 100
for i in range(0, 100, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. stars problem 1
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end='')
print()

# Another solution for question c
# number_of_stars = int(input("Number of stars: "))
# print("*"*number_of_stars)

# d. stars problem 2
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars+1):
    print("*" * i)
print()
