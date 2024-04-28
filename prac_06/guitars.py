from prac_06.guitar import Guitar

guitars = []


def main():
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added.", end="\n\n")
        name = input("Name: ")

    print("\n...snip...\n")

    print("These are my guitars:")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("Guitar Sort Result:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = "(vintage) if guitar.is_vintage() else"
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars so Quick, go and buy one")

main()
