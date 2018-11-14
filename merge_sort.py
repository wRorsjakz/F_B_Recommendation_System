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