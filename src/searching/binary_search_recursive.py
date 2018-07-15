# Returns the index of a target value in an array
# Uses binary search with recursion
# Can only find one index, not multiple
# Conditions:
# 1. The array must consist of only numbers
# 2. The array must be sorted

import math

def binary_search(array, start, end, target):
    # Recursive algorithm does not reach last index; special case
    if array[len(array)-1] == target:
        return len(array)-1
    
    if start < end:
        middle = start + math.floor((end-start)/2)
        
        if target < array[middle]:
            return binary_search(array, start, middle, target)
        elif target > array[middle]:
            return binary_search(array, middle, end, target)
        else:
            return middle

    # Return -1 if target was not found in array
    return -1
    
