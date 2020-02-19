# TO-DO: Complete the selection_sort() function below 

'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

'''

# [4,3,1,2,6,5]
# [1,|  3,4,2,6,5]
# [1,2,|  4,3,6,5]
# [1,2,3,|  4,6,5]
# [1,2,3,4,|  5,6]


def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
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

# [4,3,1,2,6,5]
# [3,4,1,2,6,5]
# [3,1,4,2,6,5]
# [3,1,2,4,6,5]
# [3,1,2,4,5,6]

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

bubbly_arr= [3,5,2,1,9,10]
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

print(selection_sort(bubbly_arr))
print(bubble_sort([3,5,2,1,9,10]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr