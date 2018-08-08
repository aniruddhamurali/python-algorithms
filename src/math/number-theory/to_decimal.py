# Converts a base 10 number to binary
# Currently only works bases <= 10

def decimal(num, base):
    if base == 10:
        return num
    total = 0
    digits = list(str(num))[::-1]
    for i in range(0,len(digits)):
        total += int(digits[i]) * base**(i)
    return total
