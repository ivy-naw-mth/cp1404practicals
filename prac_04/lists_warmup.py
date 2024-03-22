numbers = [3, 1, 4, 1, 5, 9, 2]

# print(numbers[0])-number 3
# print(numbers[-1])-number 2
# print(numbers[3])-number 1
# print(numbers[:-1])-number [3, 1, 4, 1, 5, 9]
# print(numbers[3:4])-number [1]
# print(5 in numbers)-true
# print(7 in numbers)-false
# print("3" in numbers)-false
# print(numbers + [6, 5, 3])-[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

#1. Change the first element of numbers to "ten"
numbers[0]= "ten"

#2. Change the last element of numbers to 1
numbers[-1]= 1

#3. Print all elements from numbers except the first two (slice)
print(numbers[2:7])

#4. Print whether 9 is an element of numbers
print(9 in numbers)