def parse_query_string(query_string):
    # Remove the '?' if it exists at the beginning of the query string
    if query_string.startswith('?'):
        query_string = query_string[1:]

    # Split the query string into individual parameters
    parameters = query_string.split('&')

    # Initialize an empty list to store the tuples
    result = []

    # Iterate through each parameter
    for parameter in parameters:
        # Split the parameter into name and value
        name, value = parameter.split('=')

        # Convert numeric values to numbers if possible
        if value.isdigit():
            value = int(value)

        # Append the tuple (name, value) to the result list
        result.append((name, value))

    return result


# Test the function with an example query string
query_string = "?name=Bob&age=99&day=Wed"
print(parse_query_string(query_string))
