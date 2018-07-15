# Returns sorted array using insertion sort
# Every iteration, takes an element at index i and inserts it into the sorted sequence array from indexes 0 to i-1

def insertion_sort(array):
    for i in range(0, len(array)):
        current = array[i]
        
        # Elements in array that are greater than current are moved one position to the right
        j = i-1
        while j >= 0 and current < array[j]:
            array[j+1] = array[j]
            j -= 1
            
        array[j+1] = current
        
    return array
