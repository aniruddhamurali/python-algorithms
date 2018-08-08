''' Calculates greatest common divisor of two numbers.'''
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)


''' Based on Euler’s product formula. The formula basically says that the value
    of phi(n) is equal to n multiplied by the product of (1 – 1/p) for all prime
    factors p of n.

    Much faster compared to the first program.'''
def phi(n):
    count = n
    p = 2
    while(p*p <= n):
        if n % p == 0:
            while n % p == 0:
                n = n//p
            count *= 1.0 - (1.0/float(p))
        p += 1

    if n > 1:
        count *= 1.0 - (1.0/float(n))

    return int(count)
