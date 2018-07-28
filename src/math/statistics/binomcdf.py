''' Calculates the probability that there will be 0 to x successes in n trials if
    there is a probability p of success for each trial. '''

from basic_stat import stat

# n: number of trials
# p: probability of success for each trial
# x: maximum number of wanted successes
# Binomial Probability = nCx * p^x * (1-p)^(n-x); you may know 1-p as q, the probability of failure
# Unlike binompdf(), binomcdf adds all binomial probabilities from 0 to x, inclusive
def binomcdf(n, p, x):
    total = 0
    for i in range(0,x+1):
        total += stat.combination(n, i) * p**i * (1-p)**(n-i)
    return total
