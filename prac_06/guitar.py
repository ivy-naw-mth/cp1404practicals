CURRENT_TIME = 2024

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Function for the classes"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the string"""
        return f"{self.name} ({self.year}): ${self.cost:,.2f}"

    def get_age(self):
        """This function allows it to calculate to get the age"""
        age = CURRENT_TIME - self.year
        return age

    def is_vintage(self):
        """Check if vintage or not"""
        age = self.get_age()
        if age > 50:
            return True
        else:
            return False

    def __lt__(self, other):
        """Compare 2 guitar instances based on their manufacturing years"""
        return self.year < other.year