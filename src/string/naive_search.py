# Naive search algorithm
# Checks if pattern is within the string

def naive_search(string, pattern):
    m = len(string)
    n = len(pattern)
    for i in range(m):
        for j in range(n):
            if string[i+j] != pattern[j]:
                break
            elif j == n-1:
                return i
    return None
