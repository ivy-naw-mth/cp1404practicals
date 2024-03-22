"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get the sales 
while sales >= 0 
if sales < 1000
bonus = sales * 0.1
else 
bonus = sales * 0.15
display bonus
"""

BONUS_THRESHOLD = 1000
LOWER_BONUS_RATE = 0.1
HIGHER_BONUS_RATE = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_THRESHOLD:
        bonus_rate = sales * LOWER_BONUS_RATE
    else:
        bonus_rate = sales * HIGHER_BONUS_RATE
    print("Bonus is $", bonus_rate)
    sales = float(input("Enter sales: $"))