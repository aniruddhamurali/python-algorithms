''' normalpdf can be used to calculate the normal probability density at a given
    x value. '''

from basic_stat import stat
import math

# density function for normal distribution
def d(x, mew, sigma):
    return (1/(sigma*math.sqrt(2*math.pi))) * math.exp(-1/2*((x-mew)/sigma)**2)

def normalpdf(x, mean, stdev):
    return d(x, mean, stdev)
