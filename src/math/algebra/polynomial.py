# Module for polynomial math

class Polynomial:

    ''' Creates a polynomial. When inputting the array of coefficients, start
        from the degree (highest exponent) term.'''
    def __init__(self, coefficients):
        # Reverses the input to make addition and other operations easier
        self.coefficients = coefficients[::-1]


    ''' Calling print() will display the polynomial itself.'''
    def __str__(self):
        string = ""
        # Starts to print from highest degree to constant
        for i in range(len(self.coefficients)-1, -1, -1):
            # If the coefficient is 0, no need to display
            if self.coefficients[i] == 0:
                continue

            # If the coefficient is 1 or -1, we don't need to show it by convention
            # We must show the 1 if it's a constant (applies to constants in general)
            if abs(self.coefficients[i]) != 1 or i == 0:
                # We need to deal with the sign for just the first term
                if i == len(self.coefficients)-1:
                    string += str(self.coefficients[i])
                # We already took care of the sign, so use absolute value
                else:
                    string += str(abs(self.coefficients[i]))
            
            # No x term or plus needed if we are at the constant
            if i != 0:
                string += "x^" + str(i)
                # If the next term is negative, put a minus sign
                if self.coefficients[i-1] < 0:
                    string += " - "
                else:
                    string += " + "
                    
        return string


    ''' Allows the user to modify the polynomial.'''
    def set_coefficients(self, coefficients):
        self.coefficients = coefficients[::-1]


    ''' Returns the degree of the polynomial.'''
    def degree(self):
        return len(self.coefficients)-1


    ''' Adds two polynomial objects; allows you to use the plus sign for adding two
        polynomials.'''
    def __add__(self, p):
        new_coefficients = []
        length = min(len(self.coefficients), len(p.coefficients))
        for i in range(length):
            new_coefficients.append(self.coefficients[i] + p.coefficients[i])

        # Append the extra terms
        if len(self.coefficients) > length:
            for j in range(length, len(self.coefficients)):
                new_coefficients.append(self.coefficients[j])
        elif len(p.coefficients) > length:
            for k in range(length, len(p.coefficients)):
                new_coefficients.append(p.coefficients[k])

        # Reverse new_coefficients for __init__
        new_coefficients = new_coefficients[::-1]
        new_polynomial = Polynomial(new_coefficients)
        return new_polynomial


    ''' Subtracts two polynomial objects; allows you to use the minus sign for
        subtracting two polynomials.'''
    def __sub__(self, p):
        new_coefficients = []
        length = min(len(self.coefficients), len(p.coefficients))
        for i in range(length):
            new_coefficients.append(self.coefficients[i] - p.coefficients[i])

        # Append the extra terms; is terms are from p, make them negative
        if len(self.coefficients) > length:
            for j in range(length, len(self.coefficients)):
                new_coefficients.append(self.coefficients[j])
        elif len(p.coefficients) > length:
            for k in range(length, len(p.coefficients)):
                new_coefficients.append(-1*p.coefficients[k])

        # Reverse new_coefficients for __init__
        new_coefficients = new_coefficients[::-1]
        new_polynomial = Polynomial(new_coefficients)
        return new_polynomial


    ''' Multiplies two polynomial objects; allows you to use the multiplication sign
        for multiplying two polynomials.'''
    def __mul__(self,p):
        new_coefficients = [0]*(self.degree() + p.degree()+1)

        for i in range(len(self.coefficients)):
            for j in range(len(p.coefficients)):
                # i+j is the exponent of each term
                new_coefficients[i+j] += self.coefficients[i] * p.coefficients[j]
                
        # Reverse new_coefficients for __init__
        new_coefficients = new_coefficients[::-1]
        new_polynomial = Polynomial(new_coefficients)
        return new_polynomial
            
