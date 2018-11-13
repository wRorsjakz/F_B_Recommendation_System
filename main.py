import kivy
kivy.require('1.9.0')
from kivy.config import Config
# This prevents the window from being resized

Config.set('graphics', 'resizable', False)
from kivy.core.window import Window
# This sets the window to size (800,600)
Window.size = (1000,1000)
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

    # This function retrieves the coordinates of the mouse cursor on the map
    def mouse_pos(self,window,pos):
        self.ids.cursor_coordinate_id.text = "Cursor: " + str(pos)

    # This function is called when the user clicks on the map.
    # NOTE: It does not call when the user clicks outside of the map
    # It retrieves the coordinates of the user's click
    def get_coordinates(self):
        # Console debugging
        print("User has clicked on the map.")

        # Retrieves the coordinates where the user clicked on the map
        coordinates = self.ids.cursor_coordinate_id.text.split(':')[1]

        # Appends coordinates to a label so that the user can see what he has chosen
        self.ids.chosen_coordinate_id.text = "Chosen:" + coordinates

        # Console debugging
        print("Coordinate of cursor click:",coordinates)

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