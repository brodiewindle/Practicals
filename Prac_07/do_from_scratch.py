from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DoFromScratchApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["bob", "billy", "brice", "jess", "chelsea", "scott", "tianna"]

    def build(self):
        self.title = "Do from Scratch App"
        self.root = Builder.load_file('do_from_scratch.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
