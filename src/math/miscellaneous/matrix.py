# Matrix module designed for mathematical purposes

class Matrix:

    ''' Create a matrix with the inputted number of rows and columns.'''
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = self.construct(self.rows, self.columns)


    ''' Calling print() on this Matrix will display the matrix itself.'''
    def __str__(self):
        string = ""
        for i in range(self.rows):
            string += "["
            for j in range(self.columns):
                if j == self.columns-1:
                    string += str(self.matrix[i][j])
                else:
                    string += str(self.matrix[i][j]) + " "
            string += "]\n"
        return string


    ''' Creates a null matrix with r rows and c columns.'''
    def construct(self, r, c):
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(None)
            matrix.append(row)
        return matrix


    ''' Returns the number of rows in the matrix.'''
    def numRows(self):
        return self.rows


    ''' Returns the number of columns in the matrix.'''
    def numCols(self):
        return self.columns


    ''' Assigns a value to an entry in the matrix.'''
    def assignValue(self, row, col, val):
        self.matrix[row][col] = val


    ''' To assign an entire matrix to self.matrix, you can either use assignMatrix(m),
        or directly modify the self.matrix variable.'''
    def assignMatrix(self, m):
        self.matrix = m


    ''' Adds matrix2 to self.matrix; __add__ allows you to use the plus
        sign for adding two matrices.'''
    def __add__(self, matrix2):
        if len(self.matrix) != len(matrix2) or len(self.matrix[0]) != len(matrix2[0]):
            raise Exception("Matrices must have the same dimensions")
        answer = self.construct(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                answer[i][j] = self.matrix[i][j] + matrix2.matrix[i][j]
        return answer


    ''' Subtracts matrix2 from self.matrix; __sub__ allows you to use the minus
        sign for subtracting two matrices.'''
    def __sub__(self, matrix2):
        if len(self.matrix) != len(matrix2) or len(self.matrix[0]) != len(matrix2[0]):
            raise Exception("Matrices must have the same dimensions")
        answer = self.construct(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                answer[i][j] = self.matrix[i][j] - matrix2.matrix[i][j]
        return answer


    ''' Multiplies matrix2 to self.matrix.'''
    def multiply(self, matrix2):
        answer = self.construct(self.rows, self.columns)
        # If matrix2 isn't actually a matrix but rather a scalar
        if type(matrix2) == int or type(matrix2) == float:
            for i in range(self.rows):
                for j in range(self.columns):
                    answer[i][j] = self.matrix[i][j] * matrix2
        # Otherwise if matrix2 is actually a matrix
        else:
            for i in range(self.columns):
                for j in range(len(matrix2.matrix[0])):
                    total = 0
                    for k in range(self.columns):
                        total += self.matrix[i][k] * matrix2.matrix[k][j]
                    answer[i][j] = total
        return answer


    ''' Calls multiply(); __mul__ allows you to use the minus sign for multiplying
        two matrices.'''
    def __mul__(self, matrix2):
        # number of columns in self.matrix must equal number of rows in matrix2
        if len(self.matrix[0]) != len(matrix2):
            raise Exception("The number of columns in the first matrix must equal the number of rows in the second matrix")
        return self.multiply(matrix2)


    ''' Calculates the determinant of self.matrix using recursion.'''
    def determinant(self):
        det = 0
        # Matrices with 1 or 2 rows are base cases
        if self.rows == 1:
            return self.matrix[0][0]
        elif self.rows == 2:
            return self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]

        temp = self.construct(self.rows-1, self.rows-1)
        for i in range(self.columns): # columns
            x = 0 # variable representing the column being selected
            for j in range(self.rows): # rows
                if j != i: # i column is not included
                    for k in range(1,self.rows):
                        temp[k-1][x] = self.matrix[k][j]
                    x += 1
            m = Matrix(len(temp), len(temp[0]))
            m.assignMatrix(temp)
            det += pow(-1,i) * self.matrix[0][i] * m.determinant()

        return det

    ''' rrac stands for remove row and column.'''
    def rrac(self, row, column):
        inputMatrix = self.matrix
        outputMatrix = self.construct(self.rows-1,self.columns-1)
        x = 0
        y = 0

        for i in range(self.rows):
            for j in range(self.columns):
                if i == row or j == column:
                    continue
                elif y >= len(outputMatrix):
                    break
                else:
                    outputMatrix[x][y] = self.matrix[i][j]
                    y += 1

            if i != row:
                x += 1
            y = 0

        return outputMatrix


    ''' Calculates the minors matrix.'''
    def minors(self):
        answer = self.construct(self.rows, self.columns)
        for i in range(self.columns):
            for j in range(self.rows):
                temp = self.rrac(j,i)
                m = Matrix(len(temp), len(temp[0]))
                m.assignMatrix(temp)
                answer[j][i] = m.determinant()
        return answer


    ''' Calculates the cofactors matrix.'''
    def cofactors(self):
        answer = self.construct(self.rows, self.columns)
        for i in range(self.columns):
            for j in range(self.rows):
                if (i+j) % 2 == 1:
                    answer[j][i] = -1*self.matrix[j][i]
                else:
                    answer[j][i] = self.matrix[j][i]
        return answer


    ''' Returns the transpose of self.matrix.'''
    def transpose(self):
        answer = self.construct(self.rows, self.columns)
        for i in range(self.columns):
            for j in range(self.rows):
                answer[j][i] = self.matrix[i][j]
        return answer


    ''' Calculates the inverse of self.matrix by using the minors(), cofactors(),
        and transpose() functions.'''
    def inverse(self):
        # Matrices with a determinant of 0 do not have an inverse
        if self.determinant() == 0:
            raise Exception("This matrix does not have an inverse")
        else:
            temp = self.matrix
            self.assignMatrix(self.minors())
            self.assignMatrix(self.cofactors())
            self.assignMatrix(self.transpose())
            answer = self.multiply(1/(self.determinant()))
            self.matrix = temp
            return answer
                        
    
