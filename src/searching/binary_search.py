# Returns the index of a target value in an array
# Uses binary search
# Can only find one index, not multiple
# Conditions:
# 1. The array must consist of only numbers
# 2. The array must be sorted

import math

def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = start + math.floor((end-start)/2)
        if target == array[middle]:
            return middle

        if target > array[middle]:
            start = middle + 1
        else:
            end = middle - 1

    # Return -1 if target was not found in array
    return -1
