from kivy.app import App
from kivy.lang import Builder

CONVERSION_FACTOR = 1.60934


class MphToKph(App):

    def build(self):
        self.title = "MPH to KPH converter"
        self.root = Builder.load_file('mph_to_kph.kv')
        return self.root

    def handle_increment(self, increment):
        miles = int(self.root.ids.input_number.text)
        kph = miles + increment
        self.root.ids.output_file.text = str(kph)

    def handle_conversion(self):
        miles = int(self.root.ids.input_number.text)
        kph = miles * CONVERSION_FACTOR
        self.root.output_number.text = str(kph)

    @staticmethod
    def str_to_float(text):
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


MphToKph().run()
