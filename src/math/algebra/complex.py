# Module for complex numbers

class Complex:

    ''' Creates a complex number. The first parameter is the real component, the second
        parameter is the imaginary component.'''
    def __init__(self, r, i):
        self.r = r
        self.i = i


    ''' Calling print() will display the complex number in the form a+bi.'''
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


    ''' Adds two complex number objects; allows you to use plus sign for adding complex
        numbers.'''
    def __add__(self, c):
        new_complex = Complex(self.r + c.r, self.i + c.i)
        return new_complex


    ''' Subtracts two complex number objects; allows you to use minus sign for subtracting
        complex numbers.'''
    def __sub__(self, c):
        new_complex = Complex(self.r - c.r, self.i - c.i)
        return new_complex


    ''' Multiplies two complex number objects; allows you to use the multiplication sign
        for multiplying complex numbers.'''
    def __mul__(self, c):
        if type(c) == int or type(c) == float:
            new_complex = Complex(self.r*c, self.i*c)
        else:
            # (a+bi)(c+di) = ac + adi + bci - bd
            new_complex = Complex(self.r*c.r - self.i*c.i, self.r*c.i + self.i*c.r)
        return new_complex


    ''' Divides two complex number objects; allows you to use the division sign for
        dividing complex numbers.'''
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


    ''' Calculates the absolute value of the complex number.'''
    def __abs__(self):
        return pow(self.r**2 + self.i**2, .5)


    ''' Returns the real component of the complex number.'''
    def real(self):
        return self.r


    ''' Returns the imaginary component of the complex number.'''
    def imaginary(self):
        return self.i

