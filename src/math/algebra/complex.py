
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

    def __mul__(self, c):
        if type(c) == int or type(c) == float:
            new_complex = Complex(self.r*c, self.i*c)
        else:
            # (a+bi)(c+di) = ac + adi + bci - bd
            new_complex = Complex(self.r*c.r - self.i*c.i, self.r*c.i + self.i*c.r)
        return new_complex

    def __truediv__(self, c):
        if type(c) == int or type(c) == float:
            new_complex = Complex(self.r/c, self.i/c)
        else:
            # (a+bi)/(c+di) = ((a+bi)(c-di))/((c+di)(c-di))
            # = (ac - adi + bci + bd)/(c^2 + d^2)
            # Real: (ac+bd)/(c^2+d^2)  Imaginary: (-ad+bc)/(c^2+d^2)
            new_r = (self.r*c.r + self.i*c.i)/(c.r**2 + c.i**2)
            new_i = (-1*self.r*c.i + self.i*c.r)/(c.r**2 + c.i**2)
            new_complex = Complex(new_r, new_i)
        return new_complex

