# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        # if the length of arrA == 0, and merged_arr[i] is arrB[0], 
        # then remove and return the first num in arrB
        if(len(arrA) ==0):
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        elif(len(arrB) == 0):
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif(arrA[0] <= arrB[0]):
            merged_arr[i] =arrA[0]
            arrA.pop(0)
        else:
            merged_arr[i] = arrB[0]
            arrB.pop(0)

    return merged_arr

print(merge([1, 3, 5, 7, 9,33,44,49], [2,4,6,8,12]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # start with a base case
    if len(arr) <= 1:
        return arr
    # make a mid point
    index_split = len(arr) // 2
    # separate the array into two parts -> left & right
    left_side = merge_sort(arr[:index_split])
    right_side = merge_sort(arr[index_split:])
    #Run this step repeatedly until all arrays are a length of 1

    # print("LEFT SIDE: ", left_side)
    # print("RIGHT SIDE: ", right_side)
    return(merge(left_side, right_side))
print(merge_sort([1, 3, 5, 7, 9, 32, 44, 49, 0, 2, 4, 6, 6]))







# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
