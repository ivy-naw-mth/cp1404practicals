CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

#4. A loop that prints all the states and names
for state_code in CODE_TO_NAME:
     print(f"{state_code} is {CODE_TO_NAME[state_code]}")

#5. "Easier to Ask Forgiveness than Permission"
state_code = input("Please enter state name: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:(
        print("Invalid state name."))
    state_code = input("Please enter state name: ").upper()
