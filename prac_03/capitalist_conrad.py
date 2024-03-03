import random

MAXIMUM_INCREASE = 0.175  # 10%
MAXIMUM_DECREASE = 0.05  # 5%
MINIMUM_PRICE = 1
MAXIMUM_PRICE = 100
INITIAL_PRICE = 10.0
number_of_days = 0
price = INITIAL_PRICE
OUTPUT_FILE= "capitalist_conrad_output.txt"

print(f"${price:,.2f}")
out_file = open(OUTPUT_FILE, 'w')

while MINIMUM_PRICE <= price <= MAXIMUM_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if the number is 1, the price will increase, otherwise the price will decrease.
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAXIMUM_INCREASE
        price_change = random.uniform(0, MAXIMUM_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAXIMUM_DECREASE and 0
        price_change = random.uniform(-MAXIMUM_DECREASE, 0)
    number_of_days+=1
    price *= (1 + price_change)

    print(f"On day {number_of_days} price is ${price:,.2f}")
    print(f"On day {number_of_days} price is ${price:,.2f}", file=out_file)
out_file.close()