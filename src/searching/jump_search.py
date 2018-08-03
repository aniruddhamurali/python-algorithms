# Jump search algorithm

import math

def jump_search(array, x, n):
    # Jump size = sqrt(n); this is the best step size, determined with math
    step = math.sqrt(n)
    prev = 0

    while array[int(min(step,n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1:

    while array[int(prev)] < x:
        prev += 1
        if prev == min(step,n):
            return -1

    # If the element is found
    if array[int(prev) == x:
             return prev

    return -1
