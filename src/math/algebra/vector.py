# Vector module
# Allows you to use many functions that are similar to those of lists.
# Also allows you to perform mathematical operations on a vector.

class Vector:

    ''' Create a vector by inputting an array.'''
    def __init__(self, vector):
        self.vector = vector


    ''' Calling print() will display the vector itself.'''
    def __str__(self):
        string = "< "
        for i in range(len(self.vector)):
            string += str(self.vector[i])
            if i != len(self.vector)-1:
                string += ", "
        string += " >"
        return string


    ''' Returns the number of components in the vector; allows you to use len()
        on Vector objects.'''
    def __len__(self):
        return len(self.vector)


    ''' Returns if the vector contains the given value; allows you to use the
        'in' keyword (value in Vector).'''
    def __contains__(self, value):
        for i in self.vector:
            if i == value:
                return True
        return False


    ''' Returns if two Vector objects are equal; allows you to use == to compare
        two vectors.'''
    def __eq__(self, v):
        if len(self.vector) != len(v.vector):
            return False
        for i in self.vector:
            for j in v.vector:
                if i != j:
                    return False
        return True


    ''' Returns the component of the vector at the given index.'''
    def get(self, index):
        return self.vector[index]

    ''' Returns the first index of a component in the vector.'''
    def index(self, value):
        for i in range(len(self.vector)):
            if self.vector[i] == value:
                return i
        raise Exception("Value is not a component of the vector")

    ''' Appends value onto the end of the vector.'''
    def append(self, value):
        self.vector += [value]

    ''' Inserts value right before the given index.'''
    def insert(self, index, value):
        self.vector = self.vector[:index] + [value] + self.vector[index:]

    ''' Remove a component from the vector.'''
    def remove(self, index):
        if len(self.vector) == 0:
            raise Exception("Vector is empty")
        del self.vector[index]

    ''' Removes all components of the vector.'''
    def clear(self):
        for i in range(len(self.vector)):
            del self.vector[0]

    ''' Returns the number of occurrences of the given value.'''
    def count(self, value):
        c = 0
        for i in self.vector:
            if i == value:
                c += 1
        return c

    ''' Sets a component of the vector with the given value at the given index.'''
    def component(self, index, value):
        self.vector[index] = value


    
