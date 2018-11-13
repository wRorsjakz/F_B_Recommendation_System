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
