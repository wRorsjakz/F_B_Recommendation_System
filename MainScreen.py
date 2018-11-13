import kivy
kivy.require('1.9.0')

from kivy.config import Config
# This prevents the window from being resized
Config.set('graphics', 'resizable', False)
from kivy.core.window import Window
# This sets the window to size (800,600)
Window.clearcolor = (0.2, 0.2, 0.2, 0.5)
Window.size = (1000,1000)
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from kivy.clock import Clock
from kivy.properties import ListProperty,StringProperty
from kivy.uix.listview import ListItemButton

from data import canteen_dictionary
import functions
import utility

# The main screen of the program
class MainScreen(Screen):

    def __init__(self,*args,**kwargs):
        super(MainScreen, self).__init__(**kwargs)

    # This list stores all the data to be displayed in the listView
    # When a data is appended to my_data, it will be displayed in the listview
    my_data = ListProperty()

    # This function is called when the Search by Name button is pressed
    def onSearchNameBtnClicked(self):

        # Clears all data currently in my_data
        self.my_data.clear()

        # Deletes all the data current shown in the listview
        del self.ids.main_screen_listview.adapter.data[:]

        # Gets the string from the name textinput then converts to upper case and remove trailing whitespaces
        name = self.getName().upper().strip()

        # Console debugging
        print("Main Screen Search By Name Button clicked:",name)

        # If nothing was entered by the user, it will print a message in the textinput
        if name.__len__() == 0:
            self.my_data.append("Please enter a name.")
        # If something was entered by the user, the function functions.findByName() is called
        else:
            # functions.findByName returns a dictionary of canteens
            result_dictionary = functions.findByName(canteen_dictionary, name)

            # Console debugging
            print(result_dictionary)

            # functions.findByName returns None object if there are no matches in data
            if result_dictionary is None:
                self.my_data.append("Canteen could not be found")
            else:
                # If there matches, iterate through result_dictionary and append each canteen in the listview
                # Iterates through the individual canteen's key in the dictionary (1,2, ... etc)
                for i in result_dictionary.keys():
                    # Console debugging
                    print("key:",i)
                    # Retrieves the nested dictionary in result_dictionary (which is a single canteen) using its key
                    result = result_dictionary[i]
                    # Retrieves all of the canteen's information into a string
                    string = "Name: " + result["name"]+" \n Address: " + result['address'] + ", Tel:" + result['tel'] + ", Opening hours: " \
                             + result['opening_time'] + " to " + result['closing_time'] + " \nSeating capacity: "\
                             + str(result['seating_capacity']) + ", No of stores: " + str(result['no_of_stores']) + ", Average Price"\
                             + str(result['average_price']) + " , Rating: " + str(result['rating'])
                    # Append to my_data to be shown in the listview
                    self.my_data.append(string)

    # This function is called when the Search by Price button is pressed
    def onSearchByPriceBtnClicked(self):
        # Console debugging
        print("onSearchByPriceBtnClicked pressed")

        # Clears all data currently in my_data
        self.my_data.clear()

        # Deletes all the data current shown in the listview
        del self.ids.main_screen_listview.adapter.data[:]

        # Calls the getMaxPrice() function (it performs checks on the user's input as it has to be converted to float)
        input_max_price = self.getMaxPrice()

        # Console debugging
        print("User's max price:",input_max_price)

        # Calls function.search_by_price function and stores returned list in 'result'
        result = functions.search_by_price(canteen_dictionary,input_max_price)

        # Console debugging
        print(result)

        # If no result was found, returned list is empty, hence length is 0
        if result.__len__() < 1:
            self.my_data.append("Results no found")
        else:
            # Iterates through 'result' list and appends each string onto the listview
            for i in result:
                self.my_data.append(i)

    # This function is called when the Search by Food Button is pressed
    # It calls the utility.findByFood function
    def onSearchFoodBtnClicked(self):
        # Console debugging
        print("Main Screen Search By Food Button Clicked")

        # Clears all data currently in my_data
        self.my_data.clear()

        # Deletes all the data current shown in the listview
        del self.ids.main_screen_listview.adapter.data[:]

        # Gets the string from the food textinput then converts to upper case and remove trailing whitespaces
        food = self.ids.food_textinput_id.text.strip().upper()

        # Console debugging
        print(food)

        # If the user entered nothing/only whitespaces
        if len(food) == 0:
            self.my_data.append("Please enter a food")
        # If the user did not enter nothing/only whitespaces
        else:
            # Calls functions.findByFood() function and stores returned list
            result_canteen_by_food = functions.findByFood(canteen_dictionary, food)

            # Console debugging
            print(result_canteen_by_food)

            #functions.findByFood returns None object when no results found
            if result_canteen_by_food == None:
                self.my_data.append("No result found")
            else:
                # If results found, iterate through 'result_canteen_by_food' list and append each string to listview
                for i in range(0,result_canteen_by_food.__len__(),1):
                    self.my_data.append(result_canteen_by_food[i])

    # This function is called when Sort By Rating button is pressed
    # It calls the functions.sort_by_rank function
    def onSortByRankBtnClicked(self):
        # Console Debugging
        print("onSortByRankBtnClicked Pressed")

        # Clears all data currently in my_data
        self.my_data.clear()

        # Deletes all the data current shown in the listview
        del self.ids.main_screen_listview.adapter.data[:]

        sorted_list = functions.sort_by_rank(canteen_dictionary)

        # Iterates through the 'sorted_list' list
        for element in sorted_list:
            # Console debugging
            print(element)
            # Format string
            string = "Rating --" + str(element)
            # Append each string onto the listview
            self.my_data.append(string)

    # This function is called when Sort By Price button is pressed
    # It calls the functions.sort_by_price function
    def onSortByPriceBtnClicked(self):
        # Console debugging
        print("onSortByPriceBtnClicked Pressed")

        # Clears all data currently in my_data
        self.my_data.clear()

        # Deletes all the data current shown in the listview
        del self.ids.main_screen_listview.adapter.data[:]

        sorted_list = functions.sort_by_price(canteen_dictionary)

        # Iterates through the 'sorted_list' list
        for element in sorted_list:
            # Console debugging
            print(element)
            # Format string
            string = "Price --" + str(element)
            # Append each string onto the listview
            self.my_data.append(string)
            self.ids.main_screen_listview.adapter.data = self.my_data
            self.ids.main_screen_listview._trigger_reset_populate()

    # This function is called when Sort By Seating Capacity button is pressed
    # It calls the functions.sort_by_seating_capacity() function
    def onSortBySeatingCapacityBtnClicked(self):
        # Console Debugging
        print("onSortBySeatingCapacityBtnClicked Pressed")

        # Clears all data currently in my_data
        self.my_data.clear()

        # Deletes all the data current shown in the listview
        del self.ids.main_screen_listview.adapter.data[:]

        # The list returned by functions.sort_by_seating_capacity() function is stored in sorted_list
        sorted_list = functions.sort_by_seating_capacity(canteen_dictionary)

        # Iterates through the 'sorted_list' list
        for element in sorted_list:
            # Console debugging
            print(element)
            # Format string
            string = "Seating capacity --" + str(element)
            # Append each string onto the listview
            self.my_data.append(string)

            # Triggers the listview to update according to the data inside my_data
            # Without this, there tends to be formatting/update issues
            self.ids.main_screen_listview.adapter.data = self.my_data
            self.ids.main_screen_listview._trigger_reset_populate()


    # This function is called when All Halal Food button is clicked
    # It calls the functions.retrieveHalal() function
    def onSearchHalalFoodBtnClicked(self):
        # Console Debugging
        print("onSearchHalalFoodBtnClicked Pressed")

        # Clears all data currently in my_data
        self.my_data.clear()

        # Deletes all the data current shown in the listview
        del self.ids.main_screen_listview.adapter.data[:]

        sorted_list = functions.retrieveHalal(canteen_dictionary)

        # Iterates through the 'sorted_list' list
        for element in sorted_list:
            # Console debugging
            print(element)
            # Format string
            string = "Halal Food --" + str(element)
            # Append each string onto the listview
            self.my_data.append(string)

            # Triggers the listview to update according to the data inside my_data
            # Without this, there tends to be formatting/update issues
            self.ids.main_screen_listview.adapter.data = self.my_data
            self.ids.main_screen_listview._trigger_reset_populate()

    # This function is called when All Vegetarian Food button is clicked
    # It calls the functions.retrieveVegetarian() function
    def onSearchVegetarianBtnClicked(self):
        # Console debugging
        print("onSearchVegetarianBtnClicked Pressed")

        # Clears all data currently in my_data
        self.my_data.clear()

        # Deletes all the data current shown in the listview
        del self.ids.main_screen_listview.adapter.data[:]

        sorted_list = functions.retrieveVegetarian(canteen_dictionary)

        # Iterates through the 'sorted_list' list
        for element in sorted_list:
            # Console debugging
            print(element)
            # Format string
            string = "Vegetarian Food --" + str(element)
            # Append each string onto the listview
            self.my_data.append(string)

        # Triggers the listview to update according to the data inside my_data
        # Without this, there tends to be formatting/update issues
        self.ids.main_screen_listview.adapter.data = self.my_data
        self.ids.main_screen_listview._trigger_reset_populate()

    # This function is called when the clear button is pressed
    # It clears all the text inputs in the MainScreen GUI
    def onClearBtnClicked(self):
        # Console debugging
        print("Main Screen Clear Button clicked")

        # Clears the textinputs
        self.ids.name_textinput_id.text = ""
        self.ids.food_textinput_id.text = ""
        self.ids.max_price_input_id.text = ""

        # Clears all data currently in my_data
        self.my_data.clear()

        # Deletes all the data current shown in the listview
        del self.ids.main_screen_listview.adapter.data[:]

    # This function gets the string in the canteen name text input
    # And returns the string
    def getName(self):
        # COnsole debugging
        print("getName function called")

        # Try-except suite
        try:
            # Removes leading whitespaces and returns string
            return self.ids.name_textinput_id.text.strip()

        except Exception:
            print(Exception)
            self.ids.name_textinput_id.text = "Error"

    # This function gets the text input from the max_price input text widget
    # It checks that the input from the inputtext is valid
    # If the user's input is not valid, it returns -1
    def getMaxPrice(self):
            # Try-except suite --- Catch ValueError Exception (When user inputs non-integers/float from his keyboard)
            try:
                # Removes whitespaces in the user's input
                max_price_str = self.ids.max_price_input_id.text.strip()

                # If the user did not enter nothing/only whitespaces
                if len(max_price_str) != 0:
                    # Convert string to float
                    max_price_float = float(max_price_str)

                    # Returns -1 if user entered a negative number
                    if max_price_float < 0:
                        return -1
                    # If user input is valid, return entered price
                    else:
                        return max_price_float
                else:
                    # Returns -1 if user entered nothing/only whitespaces
                    return -1
            except ValueError:
                # Console Debugging
                print(ValueError)

                return -1

