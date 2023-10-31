from dataCapture import finalData
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label


Window.size = (800,400)
red = (175, 35, 35, 20)
blue = (35, 35, 175, 20)
class gridLayout(GridLayout):
    def __init__(self, **args):
        super(gridLayout, self).__init__(**args)
        def colorPick(valueLabel):
            
            int(valueLabel)
            firstIndex = finalData.index(valueLabel)
            temp =  finalData[firstIndex][2]
            temp *= 140
            tempRGB = 35 + temp
            if temp > 0:
                world.color = (temp,35,35,20)
            else:
                world.color = (35,35,temp,20)
        self.cols = 1
        self.rows = 3
        self.row_force_default = True
        self.row_default_height = 150
        self.spacing_vertical = 1
        self.padding = 1,1
        world = Image(source='world.png')
        #world.image_ratio(2.0)
        valueLabel = Label()
        slider = Slider(min = 1880,max = 2022)
        def OnSliderValueChange(instance,value):
            valueLabel.text = str(int(value))
            return valueLabel.text

        slider.bind(value = OnSliderValueChange) 
        self.add_widget(world)
        self.add_widget(valueLabel)
        self.add_widget(slider)
        
class ClimateApp(App):
    def build(self):
        game = gridLayout()
        
       
        return game 
root = ClimateApp()
root.run()

