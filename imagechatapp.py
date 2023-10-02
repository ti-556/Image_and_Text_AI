from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_file("imagemenu.kv")

class GridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(GridLayout, self).__init__(**kwargs)
        
        self.cols = 3
        self.rows = 3
        
        self.input = Label(
            text = "user input: ",
            size_hint_y = None,
            height = 300,
            size_hint_x = None,
            width = 500
            )
        self.add_widget(self.input)
        
        self.textinput = TextInput(
            multiline = False,
            size_hint_y = None,
            height = 300,
            size_hint_x = None,
            width = 500
            )
        self.add_widget(self.textinput)
        
        self.submit = Button(
            text = "Submit", 
            background_color = (0.3, 1, 0.8, 1),
            font_size = 20,
            size_hint_y = None,
            height = 100,
            size_hint_x = None,
            width = 300
            )
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
        
        self.output = Label(
            text = "response: ",
            size_hint_y = None,
            height = 300,
            size_hint_x = None,
            width = 500
        )
        self.add_widget(self.output)
        
        self.useroutput = Label(
            text = "",
            size_hint_y = None,
            height = 300,
            size_hint_x = None,
            width = 500
            )
        self.add_widget(self.useroutput)
        
    def press(self, instance):
        userinput = self.textinput.text
        self.textinput.text = ""
        self.useroutput.text = userinput
        
    def selected(self, filename):
        self.useroutput.text = filename[0]
        
class Main(App):
    def build(self):
        return GridLayout()
        
        
if __name__ == "__main__":
    Main().run()