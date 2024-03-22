MENU = """C - Conversion from Celsius to Fahrenheit
    F - Conversion from Fahrenheit to Celsius
    Q - Quit"""

def main():
    """Temperature Conversion"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = conversion_from_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = conversion_from_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def conversion_from_celsius_to_fahrenheit(celsius):
    """Converting Celsius to Fahrenheit"""
    return celsius * 9.0 / 5 + 32

def conversion_from_fahrenheit_to_celsius(fahrenheit):
    """Converting Fahrenheit to Celius"""
    return 5 / 9 * (fahrenheit - 32)

main()