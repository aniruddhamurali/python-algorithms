''' Returns a five number summary of a dataset:
    q0: minimum
    q1: lower quartile
    q2: median
    q3: upper quartile
    q4: maximum '''

# Make sure to have basic_stat.py in the same directory
from basic_stat import stat

def fiveNumSummary(data):
    q0 = data[0]
    q2 = stat.median(data)
    q4 = data[len(data)-1]
    
    if (len(data) % 2 == 1):
        q1 = stat.median(data[:int((len(data)+1)/2)])
        q3 = stat.median(data[int((len(data)-1)/2):])
    else:
        q1 = stat.median(data[:int((len(data)+1)/2)])
        q3 = stat.median(data[int((len(data)+1)/2):])
        
    return [q0,q1,q2,q3,q4]

