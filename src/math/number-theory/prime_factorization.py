# Generates the prime factorization of a number

import math

def generate_primes(n):
        """generate_primes(n) -> list
        Returns a list of all primes <= n."""
    
        sqrtN = math.sqrt(n)

        if n < 2:
            return []
        elif n < 3:
            return [2]
        
        primes = [2]
        potentialPrimes = list(range(3,n+1,2))
        currentPrime = potentialPrimes[0]

        while currentPrime < sqrtN:
            primes.append(currentPrime)

            for i in potentialPrimes[:]:
                if i % currentPrime == 0:
                    potentialPrimes.remove(i)
            currentPrime = potentialPrimes[0]

        primes += potentialPrimes
        return primes

def primeFactors(n):
        """factory(int) -> list
        Returns the prime factors of the input as a list
        of primes in increasing order."""
        sqrtn = int(math.sqrt(n))
        primes = generate_primes(sqrtn)

        factors = []
        for i in primes:
            while n % i == 0:
                if not i in factors:
                    factors.append(i)
                n //= i

        if n != 1:
            factors.append(n)

        return factors

# Returns the prime factorization of n in the form of a dictionary
# The keys are the primes, the values are the powers
# Ex. '2': 3 means there's a 2^3
def prime_factorization(n):
    prime_pow_Dict = dict()
    prime_factors = primeFactors(n)

    for prime in prime_factors:
        power = 0
        while n % prime == 0:
            power = power + 1
            n = n/prime

        prime_pow_Dict[str(prime)] = power

    return prime_pow_Dict




    
    
