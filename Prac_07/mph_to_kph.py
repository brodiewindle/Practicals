from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

CONVERSION_FACTOR = 1.60934


class MphToKph(App):
    output_display = StringProperty()

    def build(self):
        self.title = "MPH to KPH converter"
        self.root = Builder.load_file('mph_to_kph.kv')
        Window.size = (400, 200)
        return self.root

    def handle_increment(self, text, increment):
        miles = self.str_to_float(text) + int(increment)
        self.root.ids.input_number.text = str(miles)

    def handle_conversion(self, text):
        miles = self.str_to_float(text)
        self.update_display(miles)

    def update_display(self, miles):
        self.output_display = str(miles * CONVERSION_FACTOR)

    @staticmethod
    def str_to_float(text):
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


MphToKph().run()
