from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from chat_gpt_api import chatgpt_api_call

resource_add_path("font")
LabelBase.register(DEFAULT_FONT, "NotoSansJP-Black.ttf")

Builder.load_file("imagemenu.kv")

class GridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(GridLayout, self).__init__(**kwargs)
        
        self.imageselected = False
        self.filepath = ""
        
        self.cols = 1
        
        self.input = Label(
            text = "user input: ",
            size_hint_y = None,
            height = 30,
            )
        self.add_widget(self.input)
        
        self.textinput = TextInput(
            multiline = False,
            size_hint_y = None,
            height = 100,
            )
        self.add_widget(self.textinput)
        
        self.submit = Button(
            text = "Submit", 
            background_color = (0.3, 1, 0.8, 1),
            font_size = 20,
            size_hint_y = None,
            height = 30,
            )
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)
        
        self.output = Label(
            text = "response: ",
            size_hint_y = None,
            height = 30,
        )
        self.add_widget(self.output)
        
        self.useroutput = Label(
            text = "",
            font_size = 12,
            text_size = (1500, None),
            size_hint_y = None,
            height = 500,
            valign = "top"
            )
        self.add_widget(self.useroutput)
        
    def press(self, instance):
        userinput = self.textinput.text
        if self.imageselected:
            self.useroutput.text = chatgpt_api_call(image_path = self.filepath, prompt = "")
        if not self.imageselected:
            self.useroutput.text = chatgpt_api_call(image_path = "", prompt = userinput)
        self.textinput.text = ""
        
    def selected(self, filename):
        self.filepath = filename[0]
        self.imageselected = True
        
class Main(App):
    def build(self):
        return GridLayout()
        
        
if __name__ == "__main__":
    Main().run()

        
if __name__ == "__main__":
    Main().run()
