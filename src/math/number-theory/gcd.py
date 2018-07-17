# Uses Euclidean Algorithm to calculated the GCD of 2 numbers
def gcd(x, y):
    a = max(x,y)
    b = min(x,y)

    rem = a % b

    if rem == 0:
        return b
    else:
        gcd(b, rem)
