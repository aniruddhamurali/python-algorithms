# Uses the Sieve of Eratosthenes to generate a list of primes below a number

def sieve(n):
    """Return a list of the primes below n."""
    prime = [True] * n
    result = [2]
    append = result.append
    sqrt_n = (int(n**.5) + 1) | 1 # ensure it's odd
    for p in range(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::2*p] = [False] * ((n-p*p-1) // (2*p) + 1)
    for p in range(sqrt_n, n, 2):
        if prime[p]:
            append(p)
    return result
