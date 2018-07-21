# Statistics class consisting of basic functions for single-variate data

class stat:

    ''' Calculate the mean of a dataset.'''
    def mean(data):
        return sum(data)/len(data)


    ''' Calculate the range of a dataset.'''
    def range(data):
        return max(data) - min(data)


    ''' Calculate the interquartile range of a dataset.'''
    def iqr(data):
        fiveNum = stat.fiveNumSummary(data)
        return fiveNum[3] - fiveNum[1]


    ''' Calculate the standard deviation of a dataset.'''
    def stdev(data):
        m = stat.mean(data)
        answer = 0
        for n in data:
            answer += (n-m)**2
        answer = pow(answer/(len(data)-1), 0.5)
        return answer


    ''' Calculate the variance of a dataset.'''
    def variance(data):
        return (stat.stdev(data))**2


    ''' Return the median of a dataset.'''
    def median(data):
        if (len(data) % 2 == 1): return data[int((len(data)-1)/2)]
        else:
            ind1 = data[int(len(data)/2)]
            ind2 = data[int(len(data)/2 - 1)]
            return (ind1+ind2)/2


    ''' Return the mode of a dataset.'''
    def mode(data):
        freqDict = dict()
        for n in data:
            if (str(n) not in freqDict): freqDict[str(n)] = 0
            else: freqDict[str(n)] += 1
        maxFreqIndex = list(freqDict.values()).index(max(freqDict.values()))
        return list(freqDict.keys())[maxFreqIndex]


    ''' Calculate z-score given value, mean, and standard deviation.'''
    def zscore(x, u, sd):
        return (x-u)/sd
    

    ''' Return a five number summary of a dataset:
        q0: minimum
        q1: lower quartile
        q2: median
        q3: upper quartile
        q4: maximum '''
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


    ''' Determines if a dataset has outliers.'''
    def hasOutliers(data):
        count = 0
        outliers = list()
        fiveNum = stat.fiveNumSummary(data)
        iqr = stat.iqr(data)
        upper_bound = fiveNum[3] + 1.5*iqr
        lower_bound = fiveNum[1] - 1.5*iqr
        
        for n in data:
            if (n < lower_bound) or (n > upper_bound):
                count += 1
                outliers.append(n)
                
        if len(outliers) == 0:
            print("No outliers.")
            return False
        else:
            print("Has " + str(count) + " outliers:")
            print(outliers)
            return True
