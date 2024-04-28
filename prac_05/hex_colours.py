COLOURS_TO_CODE = {
    "Absolute Zero": "#0048ba",
    "Amethyst": "#9966cc",
    "Aquamarine2": "#76eec6",
    "BlueViolet":"#8a2be2",
    "Baby Blue":"#89cff0",
    "Beige":"#f5f5dc",
    "Boysenberry":"#873260",
    "Brandeis Blue": "#0070ff",
    "Brass": "#b5a642",
    "BrickRed":"#cb4154"}

def main():
    """Validate colour name and print corresponding code"""
    color_name = validate_color_name()
    while color_name != "":
        color_code = COLOURS_TO_CODE[color_name]
        print(f"{color_code}")
        color_name = validate_color_name()

def validate_color_name():
    """Color name input and error checking"""
    color_name = input("Color Name: ").title()
    while color_name not in COLOURS_TO_CODE:
        print("Invalid Color Name")
        color_name = input("Color Name: ").title()
    return color_name

main()
