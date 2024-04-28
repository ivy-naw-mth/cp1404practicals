from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertingApp(App):
    """Kivy app for converting the miles to km"""
    output = StringProperty()

    def build(self):
        """ Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle the calculation part"""
        number = self.validating_values(text)
        self.output = str(number * MILES_TO_KM)

    def handle_increment(self, text, change):
        """Handle the up and down button"""
        number = self.validating_values(text) + change
        self.root.ids.input_number.text = str(number)

    def validating_values(self, text):
        """Receive the text and convert to float"""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertingApp().run()

