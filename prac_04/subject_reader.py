FILENAME = "subject_data.txt"

def main():
    records = get_data()
    data = data_processing(records)
    display_report(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = input_file.readlines()
    input_file.close()
    return data

def data_processing(records):
    """this print all sort of data, and then put all the data in a list"""
    dataset = []
    for line in records:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        dataset.append(parts)
    return dataset

def display_report(data):
    """Function to display the report"""
    for line in data:
        print(f"{line[0]} is taught by {line[1]} and has {line[2]} students")
        print("")


main()
