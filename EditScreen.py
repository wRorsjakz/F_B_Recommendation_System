import kivy

kivy.require('1.9.0')

from kivy.config import Config

# This prevents the window from being resized
Config.set('graphics', 'resizable', False)
from kivy.core.window import Window

# The uuid module implements Universally Unique Identifiers as described in RFC 4122.
import uuid

# This sets the window to size (800,700) pixels
Window.clearcolor = (0.2, 0.2, 0.2, 0.5)
Window.size = (800, 700)
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from utility import displayPopup
from data import canteen_dictionary, createEmptyCanteen, keys
from kivy.properties import ListProperty


class EditScreen(Screen):

    # Class constructor
    def __init__(self, **kwargs):
        super(EditScreen, self).__init__(**kwargs)

    # This list stores all the data to be displayed in the listView
    # When a data is appended to my_data, it will be displayed in the listview
    my_data = ListProperty()

    # Called before the screen is initialised
    def on_pre_enter(self):
        self.callBack()

    # Called the every time the screen is initialised
    def callBack(self):
        # Console debugging
        print("EditScreen: Initialising... ")

        # Calls the function retrieveDataForListView() (declared below) function which retrieves
        # all the data in database and displays the data in listview
        self.retrieveDataForListView()

    # Done by Gan Shyan
    # This method retrieves the data from the canteen_dictionary and formats the data
    # It then displays each piece of data in the listview
    def retrieveDataForListView(self):
        print("retrieveDataForListView() function called")
        # Gets all the keys for individual canteens from the canteen_dictionary
        # Stores it in a list
        keys_list = list(canteen_dictionary.keys())

        # Loops through all the keys in the keys_list
        # Retrieves the name and address
        for key in keys_list:
            name = canteen_dictionary[key]["name"]
            address = canteen_dictionary[key]["address"]

            # Formats the data
            string = "Name: " + name + ",Address: " + address

            # Console debugging:
            print("Key: ", key, " Name and address: ", string)

            # Appends the data to the listview
            self.my_data.append(string)

            # Triggers the listview to update according to the data inside my_data
            # Without this, there tends to be formatting/update issues
            self.ids.edit_screen_listview.adapter.data = self.my_data
            self.ids.edit_screen_listview._trigger_reset_populate()

            # Binds the onListItemSelected() function to the listview adapters
            # Will trigger the onListItemSelected() function whenever an item in the listview is clicked
            self.ids.edit_screen_listview.adapter.bind(on_selection_change=self.onListItemSelected)

    # Done by Gan Shyan
    # This function is called when the Clear Inputs button is pressed
    # It clears all the textinput
    def onClearInputsButtonClicked(self):
        # Console debugging
        print("Edit Screen Clear button clicked")

        # Clear all textinputs by appending empty strings
        self.ids.edit_name_textinput.text = ""
        self.ids.edit_address_textinput.text = ""
        self.ids.edit_tel_textinput.text = ""
        self.ids.edit_seating_capacity_textinput.text = ""
        self.ids.edit_rating_textinput.text = ""
        self.ids.edit_no_of_stores_textinput.text = ""
        self.ids.edit_opening_hour_textinput.text = ""
        self.ids.edit_closing_hour_textinput.text = ""
        self.ids.edit_x_coordinates_textinput.text = ""
        self.ids.edit_y_coordinates_textinput.text = ""
        self.ids.edit_halal_food_store_textinput.text = ""
        self.ids.edit_vegetarian_food_store_textinput.text = ""
        self.ids.edit_popular_food_store_textinput.text = ""
        self.ids.edit_average_price_textinput.text = ""

    # Function called when Refresh Button is pressed
    # Deletes all data in my_data and deletes all data in the listview
    # Retrieves data in canteen_dictionary via retrieveDataForListView()
    def onRefreshButtonClicked(self):
        # Console debugging
        print("On refresh button pressed")

        # Function declared below
        self.clearDataInListView()

        # This function retrieves the data from the canteen_dictionary to be displayed for the listview
        self.retrieveDataForListView()

    # Done by Gan Shyan
    # Function called when Insert Button is pressed
    # Inserts a new canteen dictionary into canteen_dictionary
    def onInsertButtonClicked(self):

        # Console Debugging
        print("Edit Screen Insert Button clicked")

        # Generates a unique id using the uuid module
        new_id = uuid.uuid4().int

        # Console debugging
        print(new_id)

        # Gets a new dictionary for the new canteen
        new_canteen = self.getTextInputs()

        # If user entered invalid details, .getTextInputs() would have returned None object
        if new_canteen != None:
            # Console debugging
            print("A new canteen with valid input has been entered by user")
            # Inserts the new canteen dictionary into canteen_dictionary
            canteen_dictionary[new_id] = new_canteen

            # Console debugging
            print("New canteen has been entered into database")
            displayPopup("Success", "New canteen has been entered into database", "Dismiss")
            self.onClearInputsButtonClicked()
        else:
            # Display a popup when there are None objects in the new_canteen dictionary
            displayPopup("Please enter valid inputs!", "Please enter valid inputs!", "Dismiss")

    # Done by Gan Shyan
    # This function is called when the Update button on the edit screen is pressed
    def onUpdateButtonClicked(self):
        # Console Debugging
        print("Edit Screen Update Button clicked")

        # Calls .getTextInputs() function to retrieve new inputs from textinputs
        updated_canteen = self.getTextInputs()

        # .getTextInputs() returns None object with there are invalid text inputs
        if updated_canteen != None:
            for key in canteen_dictionary.keys():
                if canteen_dictionary[key]["name"] == updated_canteen['name'] or canteen_dictionary[key]['address'] == updated_canteen['address']:
                    canteen_dictionary[key] = updated_canteen
                    # Calls onClearInputsButtonClicked() function to remove all data in textinputs
                    displayPopup("Success!","Canteen details updated successfully","Dismiss")
                    self.onClearInputsButtonClicked()
        else:
            # If updated_canteen is None Object due to invalid textinput
            displayPopup("Invalid entries!", "Please enter valid fields!","Understood")

    # Done by Gan Shyan
    # This function is called when the delete button on the edit screen is pressed
    # It is responsible for deleting the a chosen canteen from the canteen dictionary
    def onDeleteButtonClicked(self):
        # Console debugging
        print("Edit Screen Delete Button Clicked")

        # Retrieves the string from name textinput and address textinput
        name = self.ids.edit_name_textinput.text.strip()
        address = self.ids.edit_address_textinput.text.strip()

        # Iterates through all the keys in canteen_dictionary
        for key in canteen_dictionary.keys():
            # If canteen name and address equals to user's input name and address
            if canteen_dictionary[key]['name'] == name and canteen_dictionary[key]['address'] == address:
                # Deletes canteen from canteen_dictionary
                # Break out of the iteration
                del canteen_dictionary[key]
                break
        else:
            # If no such canteen exists in canteen_dictionary database, display popup
            displayPopup("No such canteen", "Canteen cannot be found in database", "Dismiss")

        # Function declared in this module
        self.onRefreshButtonClicked()
        self.onClearInputsButtonClicked()

    # Done by Gan Shyan
    # This function gets all the text in the text inputs
    # Returns a dictionary with appropriate key-value pairs
    def getTextInputs(self):

        # Creates an empty canteen dictionary with None values for each key
        new_canteen = createEmptyCanteen(keys)
        print(new_canteen)
        # Try-except suite --- If there is no exception (ValueError when trying to convert to int/float,
        # returns a dictionary
        # Except suite --- Popup box is displayed
        try:
            # For each 'suite', the first line retrieves the string from respective textinput
            # .strip() removes trailing whitespaces
            # int() or float() converts the string to necessary variable type
            new_name_str = self.ids.edit_name_textinput.text.strip()
            new_canteen['name'] = new_name_str

            new_address_str = self.ids.edit_address_textinput.text.strip()
            new_canteen['address'] = new_address_str

            new_tel_str = self.ids.edit_tel_textinput.text.strip()
            new_canteen['tel'] = new_tel_str

            new_seating_capacity_str = self.ids.edit_seating_capacity_textinput.text.strip()
            new_seating_capacity_int = int(new_seating_capacity_str)
            new_canteen['seating_capacity'] = new_seating_capacity_int

            new_rating_str = self.ids.edit_rating_textinput.text.strip()
            new_rating_float = float(new_rating_str)
            new_canteen['rating'] = new_rating_float

            new_average_price_str = self.ids.edit_average_price_textinput.text.strip()
            new_average_price_float = float(new_average_price_str)
            new_canteen['average_price'] = new_average_price_float

            new_no_of_stores_str = self.ids.edit_no_of_stores_textinput.text.strip()
            new_no_of_stores_int = int(new_no_of_stores_str)
            new_canteen['no_of_stores'] = new_no_of_stores_int

            new_opening_hour_str = self.ids.edit_opening_hour_textinput.text.strip()
            new_canteen['opening_time'] = new_opening_hour_str

            new_closing_hour_str = self.ids.edit_closing_hour_textinput.text.strip()
            new_canteen['closing_time'] = new_closing_hour_str

            new_x_coordinate_str = self.ids.edit_x_coordinates_textinput.text.strip()
            new_x_coordinate_int = float(new_x_coordinate_str)
            new_canteen['x_coordinate'] = new_x_coordinate_int

            new_y_coordinate_str = self.ids.edit_y_coordinates_textinput.text.strip()
            new_y_coordinate_int = float(new_y_coordinate_str)
            new_canteen['y_coordinate'] = new_y_coordinate_int

            new_halal_food_str = self.ids.edit_halal_food_store_textinput.text.strip()
            new_halal_food_str_list = [x.strip() for x in new_halal_food_str.split(',')]
            new_canteen['halal_foodstall'] = new_halal_food_str_list

            new_vegetarian_food_str = self.ids.edit_vegetarian_food_store_textinput.text.strip()
            new_vegetarian_food_str_list = [x.strip() for x in new_vegetarian_food_str.split(',')]
            new_canteen['vegetarian_foodstall'] = new_vegetarian_food_str_list

            new_popular_food_str = self.ids.edit_popular_food_store_textinput.text.strip()
            new_popular_food_str_list = [x.strip() for x in new_popular_food_str.split(',')]
            new_canteen['popular_food'] = new_popular_food_str_list

            # Console debugging
            print(new_canteen)

            # Iterates through all the values in the dictionary
            # Performs checks. If there are invalid inputs, then return None object
            for key in new_canteen.keys():
                element = new_canteen[key]
                # Checks if there was a textinput where the user entered nothing ( String )
                if type(element) == None:
                    return None
                # Checks if the user only entered whitespaces
                elif isinstance(element, str):
                    if len(element) == 0:
                        return None
                else:
                    # If no invalid inputs, then return dictionary
                    return new_canteen

        except Exception:
            # Console debugging
            print(Exception)
            return None

    # Done by Gan Shyan
    # This function is called when an item in the listview is selected
    # Returns the address of the selected canteen
    def onListItemSelected(self, instance):
        print("Item selected")
        try:
            # Retrieves the string inside the item selected in the listview
            element = self.ids.edit_screen_listview.adapter.selection[0].text

            # Retrieves the address of the selected item and removes trailing whitespaces
            address = element.split(",Address:")[1].strip()

            # Console debugging
            print(address)

            # This function retrieves the selected canteen from my_data database
            # and appends all the values into the edittext
            self.appendDataToListView(address)

        # When the user clicks on an already selected list item in the listview, an exception happens
        # This catches the exception. The currently selected list item is deselected
        except:
            print("onListItemSelected exception")

    # Done by Gan Shyan
    # Retrieves the canteen in the my_data database using the "address" key
    # Proceeds to append to the canteen's value into the respective edittext
    def appendDataToListView(self, address):
        for key in canteen_dictionary.keys():
            if canteen_dictionary[key]["address"] == address:
                selected_canteen = canteen_dictionary[key]
                print(selected_canteen)

                self.ids.edit_address_textinput.text = selected_canteen['address']
                self.ids.edit_name_textinput.text = selected_canteen['name']
                self.ids.edit_tel_textinput.text = selected_canteen['tel']
                self.ids.edit_seating_capacity_textinput.text = str(selected_canteen['seating_capacity'])
                self.ids.edit_rating_textinput.text = str(selected_canteen['rating'])
                self.ids.edit_average_price_textinput.text = str(selected_canteen['average_price'])
                self.ids.edit_no_of_stores_textinput.text = str(selected_canteen['no_of_stores'])
                self.ids.edit_opening_hour_textinput.text = selected_canteen['opening_time']
                self.ids.edit_closing_hour_textinput.text = selected_canteen['closing_time']
                self.ids.edit_x_coordinates_textinput.text = str(selected_canteen['x_coordinate'])
                self.ids.edit_y_coordinates_textinput.text = str(selected_canteen['y_coordinate'])

                halal_foodstalls_list = selected_canteen['halal_foodstall']
                halal_food_stalls_str = ",".join(halal_foodstalls_list)
                self.ids.edit_halal_food_store_textinput.text = halal_food_stalls_str

                vegetarian_foodstalls_list = selected_canteen['vegetarian_foodstall']
                vegetarian_foodstalls_str = ",".join(vegetarian_foodstalls_list)
                self.ids.edit_vegetarian_food_store_textinput.text = vegetarian_foodstalls_str

                popular_foodstalls_list = selected_canteen['popular_food']
                popular_foodstalls_str = ",".join(popular_foodstalls_list)
                self.ids.edit_popular_food_store_textinput.text = popular_foodstalls_str

    # Done by Gan Shyan
    # This function clears all the data current in my_data
    # Deletes all the data current shown in the listview
    def clearDataInListView(self):

        # Clears all data currently in my_data
        self.my_data.clear()

        # Deletes all the data current shown in the listview
        del self.ids.edit_screen_listview.adapter.data[:]
