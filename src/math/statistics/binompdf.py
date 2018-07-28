''' Calculates the probability that there will be x successes in n trials if
    there is a probability p of success for each trial. '''

from basic_stat import stat

# n: number of trials
# p: probability of success for each trial
# x: number of wanted successes
# Binomial Probability = nCx * p^x * (1-p)^(n-x); you may know 1-p as q, the probability of failure
def binompdf(n, p, x):
    return stat.combination(n, x) * p**x * (1-p)**(n-x)
