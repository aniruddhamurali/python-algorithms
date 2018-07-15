# Returns sorted array using bubble sort
# Repeatedly swaps adjacent elements if they are in the wrong order

def bubble_sort(array):
    for i in range(0, len(array)):
        # The last i elements are in the correct place
        for j in range(0, len(array)-i-1):
            # If the first of two consecutive elements is greater than the second, swap them
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
            
