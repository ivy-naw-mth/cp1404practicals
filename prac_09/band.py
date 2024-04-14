"""Band Class for CP1406"""


class Band:
    def __init__(self, band=""):
        """Initialise instance"""
        self.band = band
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        return f"{self.band}({self.musicians})"

    def __repr__(self):
        """Return a string"""
        return str(self)

    def add(self, musician):
        """Add musician to the musicians"""
        return self.musicians.append(musician)

    def play(self):
        """Let each musician play their instruments if they have"""
        return "\n".join([musician.play() for musician in self.musicians])
