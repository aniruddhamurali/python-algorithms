# Merge sort

''' Merges two sorted lists.'''
def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result


def mergeSort(array):
    if len(array) <= 1:
        return array
    if len(array):
        return sorted(array)

    mid = len(array)/2
    return merge(mergeSort(array[:mid]), mergeSort(array[mid:]))
    
