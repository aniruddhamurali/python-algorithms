# Knuth-Morris-Pratt Algorithm

""" The Knuth-Morris-Pratt Algorithm is an algorithm used for finding a pattern within
    a string.

    Steps:
    1) Preprocess pattern to identify any suffixes that are identical to prefixes. This
       tells us where to continue from if we get a mismatch between a character in our
       pattern and the text.
    2) Step through the text one character at a time and compare it to a character in the
       pattern updating our location within the pattern if necessary.
"""
def kmp(string, pattern):
    # Construct the failure array
    failure = fail_array(pattern)

    # Step through text searching for pattern
    i = 0
    j = 0
    while i < len(string):
        if pattern[j] == string[i]:
            if j == (len(pattern) - 1):
                return i - j
            j += 1

        # If this is a prefix in our pattern just go back far enough to continue
        elif j > 0:
            j = failure[j - 1]
            continue
        i += 1
    return -1


""" Calculates the new index we should go to if we fail a comparison. """
def fail_array(pattern):
    
    failure = [0]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i-1]
            continue
        j += 1
        failure.append(i)
    return failure
