from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label


#The bubble sort function performs the sorting of lists within lists of our interest.
def bubblesort_food(alist):
    for passnum in range(len(alist)-1):
        for i in range(len(alist)-passnum-1):

            #The statements are similar to the example on lams, except the index of the variable to be sorted is changed.
            if alist[i][1]>alist[i+1][1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1]= temp
    return alist

####################################################################
# Function: Retrieve different types (halal/vegetarian) of foodstalls of canteens
# This function retrieves the halal/vegetarian foodstalls of all canteens.
# A list containing strings of canteen names and names of halal/vegetarian foodstalls in the canteens is returned.
# Inputs:
#   Canteen database as canteen (dictionary)
#   Key name as key
# To call function:
#   retrieveType(canteen, key)
# Written on 02/11/2018 by Goh Yun Si
# Last updated on 09/11/2018
####################################################################

# Start of function
def retrieveType(canteen, key):
    # Create an empty list to append canteen names and names of halal/vegetarian foodstalls in the canteens
    canteen_type = []

    # Loop to access the foodstalls of each canteen
    for ID in list(canteen.keys()):

        # If canteen looped has halal/vegetarian foodstalls
        if canteen[ID][key]:

            # Extract name of canteen looped
            canteen_name = canteen[ID]["name"]

            # Loop to extract name of each halal/vegetarian foodstall in canteen looped
            for foodstall in range(len(canteen[ID][key])):
                # Extract name of each halal/vegetarian foodstall
                foodstall_name = canteen[ID][key][foodstall]

                # Append canteen name and name halal/vegetarian foodstall in the canteen into a list
                canteen_type.append(canteen_name + ": " + foodstall_name)

    # Return the list containing canteen names and names of halal foodstalls in the canteens
    return canteen_type


########################################################################################################################
# Function: Calculate distance between canteens and user
# This function calculates the linear distances between the user and all canteens.
# A sorted list containing canteen names (string) and their linear distances (float) from the user is returned.
# Inputs:
#   x-coordinates of the canteen as canteen_x (floar)
#   y-coordinates of the canteen as canteen_y (float)
#   Canteen database as canteen (dictionary)
# To call function:
#   calculateDistance(user_x,user_y,canteen)
# Written on 28/10/2018 by Goh Yun Si
# Last updated on 09/11/2018
########################################################################################################################


################################################# MERGE SORT FUNCTION ##################################################


# Start of function to merge and sort list of canteens by their linear distances from the user
def mergeList(left_list, right_list):
    # Create an empty list to append sorted list of canteen names and their linear distances from the user
    canteen_dist_sorted = []

    # While left list and right list has elements
    while left_list and right_list:

        # If first distance element of left list is smaller than first distance element of right list
        if left_list[0][1] < right_list[0][1]:

            # Append the first canteen and distance element of left list into a sorted list
            canteen_dist_sorted.append(left_list[0])

            # Pop the appended canteen and distance element out of left list
            left_list.pop(0)



        # If first distance element of right list is smaller than first distance element of left list
        else:

            # Append the first canteen and distance element of right list into a sorted list
            canteen_dist_sorted.append(right_list[0])

            # Pop the appended canteen and distance element out of right list
            right_list.pop(0)

    # If left list still contains elements (remaining distance element will be largest)
    if left_list:

        # Append the remaining elements to end of sorted list
        canteen_dist_sorted.extend(left_list)



    # If right list still contains elements (remaining distance element will be largest)
    else:

        # Append the remaining elements to end of sorted list
        canteen_dist_sorted.extend(right_list)

    # Return sorted and merged list of canteen names and their linear distances from the user
    return canteen_dist_sorted


# Start of function to split, sort, and merge list of canteens by their linear distances from the user
def mergeSort(canteen_distance_unsorted):
    # Find the number of canteen and distance elements to be sorted
    list_len = len(canteen_distance_unsorted)

    # Base case
    # If there is only 1 canteen and distance element, there is no need for sorting
    if list_len < 2:
        # Return the single canteen and distance element
        return canteen_distance_unsorted

    # If there is more than 1 canteen and distance element, split the list into half
    left_list = canteen_distance_unsorted[:list_len // 2]  # Left list: first half of canteen and distance elements
    right_list = canteen_distance_unsorted[list_len // 2:]  # Right list: second half of canteen and distance elements

    # Split, sort, and merge left and right list recursively
    left_list = mergeSort(left_list)  # Left list
    right_list = mergeSort(right_list)  # Right list

    # Return sorted and merged list of canteen names and their linear distances from the user
    return mergeList(left_list, right_list)


#################################################### MAIN FUNCTION #####################################################


# Import square root function from math module
from math import sqrt


# Start of function to calculate linear distances between canteens and user
def calculateDistance(user_x, user_y, canteen):
    # Create an empty list to append unsorted canteen names and their linear distances from the user
    canteen_distance_unsorted = []

    # Loop to extract location of each canteen
    for ID in list(canteen.keys()):
        # Extract x-coordinate of canteen looped from canteen database
        canteen_x = canteen[ID]["x_coordinate"]

        # Extract y-coordinate of canteen looped from canteen databse
        canteen_y = canteen[ID]["y_coordinate"]

        # Calculate the horizontal component of the distance between the user and the canteen looped
        distance_x = abs(user_x - canteen_x)

        # Calculate the vertical component of the distance between the user and the canteen looped
        distance_y = abs(user_y - canteen_y)

        # Calculate the total linear distance between the user and the canteen looped
        distance = sqrt(distance_x ** 2 + distance_y ** 2)

        # Append canteen name and its linear distance from the user into a list
        canteen_distance_unsorted.append([canteen[ID]["name"], distance])

    # Sort list by distances (ascending)
    canteen_dist_sorted = mergeSort(canteen_distance_unsorted)

    # Return the sorted list of canteen names and their linear distances from the user
    return canteen_dist_sorted


# Displays popup on screen with one button to dismiss it
# Takes in 3 arguements - title: Title of the popup; label_message: message inside the popup
# button_message - Text shown on the button
def displayPopup(title,label_message,button_message):
    content = BoxLayout(padding=10, orientation='vertical')
    label = Label(text=title, halign='center')
    dismiss_button = Button(text=button_message, size_hint=(None, None), size=(350, 80), halign='center')
    content.add_widget(label)
    content.add_widget(dismiss_button)
    popup = Popup(title=label_message, title_align='center', content=content,
                  auto_dismiss=False, size_hint=(None, None), size=(400, 400))
    # Binds the .dismiss function which closes the popup onto the button
    dismiss_button.bind(on_press=popup.dismiss)

    # Displays popup
    popup.open()
