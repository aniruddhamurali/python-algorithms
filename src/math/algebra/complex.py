
class Complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        string = str(self.r)
        if self.i > 0:
            string += "+" + str(self.i)
        elif self.i < 0:
            string += "-" + str(abs(self.i))
        string += "i"
        return string
        
