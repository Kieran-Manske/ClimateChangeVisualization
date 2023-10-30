from dataCapture import finalData
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class ClimateApp(App):
    def build(self):
        game = gridLayout()
        return game
    
def colorSpectrum(finalData):
    

class gridLayout(GridLayout):
    def __init__(self, **args):
        super(gridLayout, self).__init__(**args)
        self.cols = 2
        self.rows = 1
        world = Image(source='World_green_cnamed.jpg')
        self.add_widget(world)
        
        self.add_widget(Button(text = "Hello World"))

root = ClimateApp()
root.run()

