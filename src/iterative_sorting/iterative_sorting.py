# TO-DO: Complete the selection_sort() function below 

'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

'''


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        element1 = arr[i]
        element2 = arr[smallest_index]
        arr[i] = element2
        arr[smallest_index] = element1

        # arr[i], smallest_index[i] = smallest_index[i], arr[i]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    bubble_len = len(arr)
    for i in range(len(arr)):
        for j in range(0, bubble_len-i-1):
            if arr[j] > arr[j+1]:
                #swap if the element found is greater
                # than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bubble_sort(arr):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        # iterate through the array and see if any swaps have ocurred 
        for i in range(0, len(arr)-1):
            # if the element is larger, swap it to the right
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                has_swapped = True
                break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr