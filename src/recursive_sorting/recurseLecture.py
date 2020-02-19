#-------------
    # Think of recursion by solving the smallest relevant/full problem
    # [4,7,3,1]
    # [4][7][3][1]
    # [4,7][1,3]
    # []

#------------


# [7,4,8] [1,2,9,3]
# [7] [4,8] [1,2] [9,3]
# [7] [] [4] [8] [1] [2] [9] [3]

# [7][4,8][1,2][3,9]
# [4,7,8] [1,2,3,9]
# [1,2,3,4,7,8,9]

#   i
# a[4,7,8]
# b[1,2,3,9]
#   k



    # do this by -> 
    # compare the first element of each
    # add the smallest to the merged array
    # iterate the pointer for the smaller value
    # if one pointer reaches the end of it's array
    # push all remaining values in the other array to the end of merge
    #
def merge(arrA, arrB):
    elements= len(arrA) + len(arrB)
    merged_arr = [0] * elements 
    # Given two arrays 
    # combine them into a sorted array
    a = 0 
    b = 0

    for i in range(0, elements):
        # if a is done
        if a >= len(arrA):
            merged_arr(i) = arrB(b)
            b += 1
        # if b is done
        if b >= len(arrB):
            merged_arr(i) = arrA(a)
            a += 1
        # if a is smaller
        elif arrA(a) <= arrB(b):
            merged_arr(i) = arrA(a)
            a += 1
        # if b is smaller
        else:
            merged_arr(i) = arrB(b)
            b += 1







# base case
# Find middle of array with 1/2
# divide to left and right
# do merge sort on left and right (because this further divides)
# Put it back together by merging left and right

def merge_sort(arr):
    if len(arr) <= 1:

        left = merge_sort(arr[0: len(arr) // 2 ])
        right = merge_sort(arr[ len(arr) //2 :])

    
        arr = merge(left, right)
    return arr

    

   