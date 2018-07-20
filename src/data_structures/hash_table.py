# Hash table module; similar purpose and structure as dictionaries

class HashTable:

    ''' Create a hash table with size m.'''
    def __init__(self, m):
        # m is the size of tha array, r can be any prime number
        self.m = m
        self.r = 31
        self.hashtable = []
        self.construct()


    ''' Initial setup for hash table.'''
    def construct(self):
        for i in range(self.m):
            self.hashtable.append([None, None])


    ''' Calling print() on this HashTable will print the hash table itself.'''
    def __str__(self):
        string = ""
        for i in range(self.m):
            for j in range(0,len(self.hashtable[i]),2):
                
                # Only print items with a key and/or value in them
                if None not in self.hashtable[i]:
                    # Series of if/elif/else statements is for correct concatenation
                    
                    # If both the key and value are not strings
                    if type(self.hashtable[i][j]) != str and type(self.hashtable[i][j+1]) != str:
                        string += str(self.hashtable[i][j]) + ": " + str(self.hashtable[i][j+1])

                    # If only the key is not a string
                    if type(self.hashtable[i][j]) != str:
                        string += str(self.hashtable[i][j]) + ": " + self.hashtable[i][j+1]
                        
                    # If only the value is not a string
                    elif type(self.hashtable[i][j+1]) != str:
                        string += self.hashtable[i][j] + ": " + str(self.hashtable[i][j+1])
                        
                    # Otherwise if both key and value are strings
                    else:
                        string += self.hashtable[i][j] + ": " + self.hashtable[i][j+1]
                        
                    string += "\n"
                    
        return string


    ''' Calculates hash for a string and puts the string in the respective index
        of the hash table.'''
    def hash(self, s):
        h = 0 # hash
        for i in range(len(s)):
            h = (self.r * h + ord(s[i])) % self.m
        return h


    ''' Inserts key-value pair into hash table.'''
    def put(self, k, v):
        index = self.hash(k)
        if self.hashtable[index][0] == None:
            self.hashtable[index][0] = k
            self.hashtable[index][1] = v
        else:
            # This allows multiple key-value pairs to be stored in a single hash
            self.hashtable[index].append(k)
            self.hashtable[index].append(v)


    ''' Searches for a key in the hash table.'''
    def find(self, k):
        k = k.lower()
        index = self.hash(k)
        # Having a step of 2 ensures we only check keys
        for i in range(0,len(self.hashtable[index]),2):
            if self.hashtable[index][i] == k:
                return True
        return False


    ''' Gets the value given a key.'''
    def getValue(self, k):
        index = self.hash(k)
        # Having a step of 2 ensures we only check values
        for i in range(0,len(self.hashtable[index]),2):
            if self.hashtable[index][i] == k:
                # i+1 because there's a value after every key
                return self.hashtable[index][i+1]
        # If key is not in the hash table, return an error
        return "ERROR: Key does not exist"


    ''' Returns an array of the keys.'''
    def keys(self):
        keysArray = []
        for i in range(self.m):
            for j in range(0,len(self.hashtable[i]),2):
                keysArray.append(self.hashtable[i][j])
        return keysArray


    ''' Returns an array of the values.'''
    def values(self):
        valuesArray = []
        for i in range(self.m):
            for j in range(1,len(self.hashtable[i]),2):
                valuesArray.append(self.hashtable[i][j])
        return valuesArray
        
