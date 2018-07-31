# Rabin-Karp Algorithm
# Checks if pattern is within the string using hashes

def rabin_karp(string, pattern):
    m = len(string)
    n = len(pattern)
    hash_pattern = hash(pattern)
    for i in range(m):
        hash_string = hash(string[i:i+n])
        if hash_string == hash_pattern:
            if string[i:i+n] == pattern:
                return i
    return None
