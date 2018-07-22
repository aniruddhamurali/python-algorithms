''' Calculates the Hamming Distance between two strings
    Hamming Distance between two strings is the number of positions at which the
    corresponding characters are different.
    Requires that the two strings are of equal length. '''

def hamming_distance(a, b):
    if len(a) != len(b):
        raise Exception("Strings must be of the same length")
    dist = 0
    for i in range(0,len(a)):
        if a[i] != b[i]:
            dist += 1
    return dist
