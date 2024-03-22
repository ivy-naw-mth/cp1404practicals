DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > DISCOUNT_THRESHOLD:
    discount_amount = total_price * DISCOUNT_RATE
    total_price -= discount_amount

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
