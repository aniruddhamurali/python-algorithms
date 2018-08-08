''' Calculates greatest common divisor of two numbers.'''
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
''' Simple method: Iterate through all numbers from 1 to n-1 and count numbers
    with gcd with n as 1.'''
def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result
