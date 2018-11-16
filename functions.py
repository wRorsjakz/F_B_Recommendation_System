# Import functions from modules
from utility import retrieveType
from bubble_sort import bubblesort_food


# Done by He Wanru
# This function sorts the ratings of each canteen by ascending order for user reference.
# This sorting function consists of 2 parts:
#   1) appending values of the main dictionary into an empty list
#   2) the sorting itself.

# This is the main function which appends the values from the main dictionary ("canteen_dictionary") into an empty list and calls the bubble sort function.
def sort_by_rank(canteen):
    # An empty list, "canteen_rank" is created for appending of values from the main dictionary
    canteen_rank = []

    # Another empty list, "temp", is created to convert the lists within "canteen_rating" into strings with the following format
    temp = []

    # The name value and rating value are appended into the "canteen_rank"
    for ID in list(canteen.keys()):
        canteen_name = canteen[ID]["name"]
        ranking = canteen[ID]["rating"]
        canteen_rank.append([canteen_name, ranking])

    # The bubble sort function is called to sort the ratings in ascending order and a new sorted list "canteen_rating" is created
    canteen_rating = bubblesort_food(canteen_rank)

    # The lists in "canteen_rating" are converted to strings for greater readability.
    for place in canteen_rating:
        temp.append(place[0] + " : " + str(place[1]))
    return temp


# Done by He Wanru
# This search function enables users to refer to a list of canteens with average price lower or equals to how much they are willing to spend on a meal.
# This search function consists of 3 parts:
#   1) fetching of data from "canteen_dictionary"
#   2) sorting of data according to ascending order
#   3) converting lists into strings for better readability.

# This is the main function which will perform the search
# Returns all canteens with price less than or equals to the input max price
def search_by_price(canteen, price):
    # An empty list is created first, where elements will be added in the later half of the function
    canteen_price = []
    # The value input by the user is assigned to "price_wanted"
    price_wanted = price
    # Another temporary list is created to convert lists within "canteen_price" to strings for better representation
    temp = []

    # All canteens with price less than or equals to the value input will be appended to "canteen_price"
    for ID in list(canteen.keys()):
        if float(canteen[ID]["average_price"]) <= price_wanted:
            canteen_name = canteen[ID]["name"]
            average_price = canteen[ID]["average_price"]
            canteen_price.append([canteen_name, average_price])

    # The bubble sort function is called here, such that the lists in "canteen_price"
    # are arranged according to ascending order of price. This improves readability.
    canteen_price = bubblesort_food(canteen_price)

    # The lists in "canteen_price" are converted to strings in the following format,
    # and a new completed list, "temp", is generated.
    for place in canteen_price:
        temp.append(place[0] + " : " + str(place[1]))
    return temp


# Done by He Wanru
# This function sorts the average prices of each canteen by ascending order for user reference.
# This sorting function consists of 2 parts: appending values of the main dictionary into an empty list and the sorting itself.
# This is the main function which appends the values from the main dictionary ("canteen_dictionary") into an empty list and calls the bubble sort function.
def sort_by_price(canteen):
    # An empty list, "canteen_price1" is created for appending of values from the main dictionary
    canteen_price1 = []

    # Another empty list, "temp", is created to convert the lists within "canteen_price2" into strings with the following format
    temp = []

    # The name value and average price value are appended into the "canteen_price1"
    for ID in list(canteen.keys()):
        canteen_name = canteen[ID]["name"]
        prices = canteen[ID]["average_price"]
        canteen_price1.append([canteen_name, prices])

    # The bubble sort function is called to sort the average prices in ascending order and a new sorted list "canteen_price2" is created
    from bubble_sort import bubblesort_food
    canteen_price2 = bubblesort_food(canteen_price1)

    # The lists in "canteen_price2" are converted to strings for greater readability.
    for place in canteen_price2:
        temp.append(place[0] + " : " + str(place[1]))
    return temp


# Done by He Wanru
# This function sorts the seating capacity of each canteen by ascending order for user reference.
# This sorting function consists of 2 parts: appending values of the main dictionary
# into an empty list and the sorting itself.
# This is the main function which appends the values from the main dictionary ("canteen_dictionary")
# into an empty list and calls the bubble sort function.

def sort_by_seating_capacity(canteen):
    # An empty list, "canteen_seat" is created for appending of values from the main dictionary
    canteen_seat = []

    # Another empty list, "temp", is created to convert the lists within "canteen_capacity" into strings with the following format
    temp = []

    # The name value and seating capacity value are appended into the "canteen_seat"
    for ID in list(canteen.keys()):
        canteen_name = canteen[ID]["name"]
        seating = canteen[ID]["seating_capacity"]
        canteen_seat.append([canteen_name, seating])

    # The bubble sort function is imported to sort the seating capacities in ascending order and a new sorted list "canteen_capacity" is created
    from bubble_sort import bubblesort_food
    canteen_capacity = bubblesort_food(canteen_seat)

    # The lists in "canteen_capacity" are converted to strings for greater readability.
    for place in canteen_capacity:
        temp.append(place[0] + " : " + str(place[1]))
    return temp


########################################################################################################################
# Function: Find canteens by food
# This function finds the canteens with the food requested by the user.
# A list containing the strings of canteen names food similar to the requested food is returned.
# Inputs:
#   Canteen database as canteen (dictionary)
#   Food requested by user as input_food (string)
# To call function:
#   findByFood(canteen, input_food)
# Written on 31/10/2018 by Goh Yun Si
# Last up dated on 09/11/2018
########################################################################################################################

# Start of function
def findByFood(canteen, input_food):
    # Create an empty list to append canteen names and food similar to the requested food
    canteen_match = []

    # Loop to search through food list of each canteen
    for ID in list(canteen.keys()):

        # Extract food list of the canteen looped
        food_list = canteen[ID]["popular_food"]

        # Loop to search through each food in the canteen looped
        for item in range(len(food_list)):

            # Extract the food in the canteen looped
            food = food_list[item]

            # If the food is similar to the requested food (in uppercase)
            # (i.e. contains keywords of the requested food)
            if input_food.upper() in food.upper():
                # Format canteen name and food name
                str_output = canteen[ID]["name"] + ": " + food

                # Append the canteen name and the food similar to the requested food
                canteen_match.append(str_output)

    # If the requested food cannot be found in any canteen
    # (i.e. canteen_match list is empty)
    if not canteen_match:
        # Returns None Object with no match can be found
        return None

    # Return the list containing the canteen names and lists of food similar to the requested food
    return canteen_match


########################################################################################################################
# Function: Find canteens by name
# This function finds the canteens with the name specified by the user.
# A dictionary containing the dictionaries of the canteens requested is returned.
# Inputs:
#   Canteen database as canteen (dictionary)
#   Canteen name as canteen_name
# To call function:
#   findByName(canteen, canteen_name)
# Written on 31/10/2018 by Goh Yun Si
# Last updated on 09/11/2018
########################################################################################################################

# Start of function
# This functions loops through a dictionary to search for a canteen with the same/similar name
def findByName(canteen, canteen_name):
    # Loop to search through name of each canteen
    # Create an empty dictionary to append dictionaries of canteens similar to requested canteen
    canteen_match = {}

    # Loop to search through names of each canteen
    for ID in list(canteen.keys()):

        # If the name of the canteen looped is similar to the requested canteen
        # (i.e. contains keywords of the requested canteen)
        if canteen_name.upper() in canteen[ID]["name"].upper():
            # Extract the dictionary of the canteen looped
            canteen_info = canteen[ID]

            # Append the dictionary of the canteen looped into a dictionary
            canteen_match[ID] = canteen_info

    # If the requested canteen cannot be found
    # (i.e. canteen_match dictionary is empty)
    if not canteen_match:
        # Returns None Object if there are no matches
        return None

    # Return the dictionary containing dictionaries of canteens similar to requested canteen
    return canteen_match


#############################################################################
# Function: Retrieve halal foodstalls of canteens
# This function retrieves the halal foodstalls of all canteens.
# A list containing strings of canteen names and names of halal foodstalls in the canteens is returned.
# Inputs:
#   Canteen database as canteen (dictionary)
# To call function:
#   retrieveHalal(canteen)
# Written on 02/11/2018 by Goh Yun Si
# Last updated on 09/11/2018
#############################################################################
def retrieveHalal(canteen):
    # Retrieves a list of canteen names and names of halal foodstalls in the canteens
    canteen_halal = retrieveType(canteen, "halal_foodstall")

    # Return the list containing canteen names and names of halal foodstalls in the canteens
    return canteen_halal


##################################################################################################################################
# Function: Retrieve vegetarian foodstalls of canteens
# This function retrieves the vegetarian foodstalls of all canteens.
# A list containing strings of canteen names and names of vegetarian foodstalls in the canteens is returned.
# Inputs:
#   Canteen database as canteen (dictionary)
# To call function:
#   retrieveVegetarian(canteen)
# Written on 02/11/2018 by Goh Yun Si
# Last updated on 09/11/2018
##################################################################################################################################

# Start of function
def retrieveVegetarian(canteen):
    # Retrieves a list of canteen names and names of vegetarian foodstalls in the canteens
    canteen_vegetarian = retrieveType(canteen, "vegetarian_foodstall")

    # Return the list containing canteen names and names of vegetarian foodstalls in the canteens
    return canteen_vegetarian
