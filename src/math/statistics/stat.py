
class stat:

    def mean(data):
        return sum(data)/len(data)


    def range(data):
        return max(data) - min(data)


    def iqr(data):
        fiveNum = stat.fiveNumSummary(data)
        return fiveNum[3] - fiveNum[1]


    def stdev(data):
        m = stat.mean(data)
        answer = 0
        for n in data:
            answer += (n-m)**2
        answer = pow(answer/(len(data)-1), 0.5)
        return answer


    def variance(data):
        return (stat.stdev(data))**2


    def median(data):
        if (len(data) % 2 == 1): return data[int((len(data)-1)/2)]
        else:
            ind1 = data[int(len(data)/2)]
            ind2 = data[int(len(data)/2 - 1)]
            return (ind1+ind2)/2


    def mode(data):
        freqDict = dict()
        for n in data:
            if (str(n) not in freqDict): freqDict[str(n)] = 0
            else: freqDict[str(n)] += 1
        maxFreqIndex = list(freqDict.values()).index(max(freqDict.values()))
        return list(freqDict.keys())[maxFreqIndex]


    def zscore(x, u, sd):
        return (x-u)/sd
    
    
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
