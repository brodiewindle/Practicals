from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DoFromScratchApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob", "Billy", "Brice", "Jess", "Chelsea", "Scott", "Tianna"]

    def build(self):
        self.title = "Do from Scratch App"
        self.root = Builder.load_file('do_from_scratch.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            # temp_label.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_label)


DoFromScratchApp().run()
