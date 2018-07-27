''' normalcdf can be used to find the probability that a random variable will
    fall in a certain interval, assuming the variable is normally distributed. '''

from basic_stat import stat
import math

# density function for normal distribution
def d(x, mew, sigma):
    return (1/(sigma*math.sqrt(2*math.pi))) * math.exp(-1/2*((x-mew)/sigma)**2)

def integral(startX, endX, numRect, mew, sigma):
    width = (endX - startX)/numRect
    total = 0
    for i in range(1,numRect):
      height = d(startX + i * width, mew, sigma)
      area = height * width
      total += area
    return total

''' Calculates area on a normal distribution from lower bound to upper bound.'''
def normalcdf(lb, ub, mean, stdev):
    # 100000 is the number of rectangles used to calculate an integral
    # It's an arbitrary value 
    # Higher number means higher accuracy, but more processing time
    return integral(lb, ub, 100000, mean, stdev)
