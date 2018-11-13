import kivy
kivy.require('1.9.0')
from kivy.config import Config
# This prevents the window from being resized

Config.set('graphics', 'resizable', False)
from kivy.core.window import Window
# This sets the window to size (800,600)
Window.size = (800,700)
# Sets the colour of the window background
Window.clearcolor = (0.2, 0.2, 0.2, 0.5)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from MainScreen import MainScreen
from EditScreen import EditScreen

MainScreen = MainScreen()
EditScreen = EditScreen()


class MapScreen(Screen):
    # Returns coordinates of mouse on the screen
    def __init__(self, **kwargs):
        super(MapScreen,self).__init__(**kwargs)
        Window.bind(mouse_pos=self.mouse_pos)

    def mouse_pos(self,window,pos):
        self.ids.x_coordinate_id.text = str(pos)

class ScreenManagement(ScreenManager):
    pass


# Loads the .kv file to draw the widgets
display = Builder.load_file("Recommendation.kv")


# Main Entry point of the app
class RecommendationApp(App):
    def build(self):
        return display


mainApp = RecommendationApp()
mainApp.run()