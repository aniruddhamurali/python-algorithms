''' Determines if a dataset has outliers.'''

# Make sure to have basic_stat.py and five_number_summary.py in the same directory
from basic_stat import stat
import five_number_summary

def hasOutliers(data):
    count = 0
    outliers = list()
    fiveNum = five_number_summary.fiveNumSummary(data)
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
