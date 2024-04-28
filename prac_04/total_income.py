def main():
    """Display the income report of incomes for a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for number_of_months in range(1, number_of_months + 1):
        income = float(input("Enter income for month " + str(number_of_months) + ": "))
        incomes.append(income)

    report(number_of_months, incomes)

def report(number_of_months, incomes):
    """Display the report of income for each month and total incomes for all months"""
    print("\nIncome Report\n-------------")
    total = 0
    for number_of_months in range(1, number_of_months + 1):
        income = incomes[number_of_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(number_of_months, income, total))

main()