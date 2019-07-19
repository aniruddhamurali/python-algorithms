# Returns sorted array using selection sort
# Indirectly maintains two subarrays: one that is sorted, one that is unsorted
# Every iteration, the minimum value in the unsorted array is moved to the end of the sorted array

def selection_sort(array):
    for i in range(0, len(array)):
        min_index = i
        
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Swap current value with minimum value in list with indices i through len(array) - 1
        array[i], array[min_index] = array[min_index], array[i]
        print(array)

    return array
