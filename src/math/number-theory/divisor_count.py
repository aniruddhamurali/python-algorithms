# This program counts the number of divisors of a number

import math

def num_divisors(n):
    numDivisor = 0
    for divisor in range(1,round(math.sqrt(n))):
        if n % divisor == 0:
            numDivisor = numDivisor + 2

    sqrtn = math.sqrt(n)
    if int(sqrtn) == float(sqrtn):
        numDivisor = numDivisor + 1

    return numDivisor
