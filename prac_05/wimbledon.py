FILENAME = "wimbledon.csv"

def main():
    """Read and display champions and winning countries information"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
    champions = extract_data(data, 2)
    countries = extract_data(data, 1)
    country_counts = count_items(countries)
    champion_counts = count_items(champions)

    print("Wimbledon Champions:")
    for name in sorted(champion_counts.keys()):
        print(f"{name}: {champion_counts[name]}")

    sorted_countries = sorted(country_counts.keys())
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))

def extract_data(data, number):
    """Get the data and number"""
    items = []
    for line in data[1:]:
        items.append(line.strip().split(",")[number])
    return items

def count_items(items):
    """Get the item counts"""
    item_counts = {}
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    return item_counts

main()

