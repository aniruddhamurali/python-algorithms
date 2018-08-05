# Quick sort

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)// 2]
    left = [i for i in array if i < pivot]
    middle = [j for j in array if j == pivot]
    right = [k for k in array if k > pivot]
    return quick_sort(left) + middle + quick_sort(right)
