def reverse_digits(num):
    '''Reverses a number.'''
    
    string = str(num)
    reverse = string[::-1]
    return int(reverse)

def palindrome(num):
    '''prints True or False according to whether or not
    num is a palindrome.'''
    
    if num == reverse_digits(num):
        return True
    else:
        return False
