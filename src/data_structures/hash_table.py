# Hash table module; similar purpose and structure as dictionaries

class HashTable:

    ''' Create a hash table with size m.'''
    def __init__(self, m):
        # m is the size of tha array, r can be any prime number
        self.m = m
        self.r = 31
        self.hashtable = []


    ''' Calculates hash for a string and puts the string in the respective index
        of the hash table.'''
    def hash(s):
        h = 0 # hash
        for i in range(len(s)):
            h = (self.r * h + s[i]) % self.m
        return h


    ''' Inserts key-value pair into hash table.'''
    def put(k, v):
        index = self.hash(k)
        if self.hashtable[index][0] == None:
            self.hashtable[index][0] = k
            self.hashtable[index][1] = v
        else:
            # This allows multiple key-value pairs to be stored in a single hash
            self.hashtable[index].append(k)
            self.hashtable[index].append(v)


    ''' Searches for a key in the hash table.'''
    def find(k):
        k = k.lower()
        index = self.hash(k)
        # Having a step of 2 ensures we only check keys
        for i in range(0,len(self.hashtable[index]),2):
            if self.hashtable[index][i] == k:
                return True
        return False


    ''' Gets the value given a key.'''
    def getValue(k):
        index = self.hash(k)
        # Having a step of 2 ensures we only check values
        for i in range(0,len(self.hashtable[index]),2):
            if self.hashtable[index][i] == k:
                # i+1 because there's a value after every key
                return self.hashtable[index][i+1]
        # If key is not in the hash table, return an error
        return "ERROR: Key does not exist"


    ''' Returns an array of the keys.'''
    def keys():
        keysArray = []
        for i in range(self.m):
            for j in range(0,len(self.hashtable[i]),2):
                keysArray.append(self.hashtable[i][j])
        return keysArray


    ''' Returns an array of the values.'''
    def values():
        valuesArray = []
        for i in range(self.m):
            for j in range(1,len(self.hashtable[i]),2):
                valuesArray.append(self.hashtable[i][j])
        return valuesArray
        
