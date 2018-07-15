# Returns indices of all target values found in an array
# Uses linear search

def linear_search(array, target):
    indices = []
    for i in range(0,len(array)):
        if array[i] == target:
            indices.append(i)
            
    if len(indices) == 0:
        print("The item you are searching is not in this array")
    return indices
        
