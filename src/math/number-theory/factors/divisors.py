# Returns a list of the factors of a number

import math

def divisors(n):
    divisorList = []
    for divisor in range(1, round(math.sqrt(n)) + 1):
        if n % divisor == 0:
            divisorList.append(divisor)
            if divisor == n//divisor:
                continue
            else:
                divisorList.append(n//divisor)
    return divisorList
