
class Complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        string = ""
        if self.r == 0:
            if self.i != 0:
                string += str(self.i) + "i"
            else:
                string += "0"
        else:
            string += str(self.r)
            if self.i > 0:
                if self.i == 1:
                    string += "+" + "i"
                else:
                    string += "+" + str(self.i) + "i"
            elif self.i < 0:
                if self.i == -1:
                    string += "-" + "i"
                else:
                    string += "-" + str(abs(self.i)) + "i"
        return string

    def __add__(self, c):
        new_complex = Complex(self.r + c.r, self.i + c.i)
        return new_complex

    def __sub__(self, c):
        new_complex = Complex(self.r - c.r, self.i - c.i)
        return new_complex
