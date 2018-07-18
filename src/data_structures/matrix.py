
class Matrix:

    ''' Create a matrix with the inputted number of rows and columns.'''
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = self.construct()

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

    ''' Creates a null matrix with rows and columns set in __init__.'''
    def construct(self):
        matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
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
        answer = self.construct()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                answer[i][j] = self.matrix[i][j] + matrix2.matrix[i][j]
        return answer

    ''' Subtracts matrix2 from self.matrix; __sub__ allows you to use the minus
        sign for subtracting two matrices.'''
    def __sub__(self, matrix2):
        answer = self.construct()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                answer[i][j] = self.matrix[i][j] + matrix2.matrix[i][j]
        return answer

    ''' Multiplies matrix2 to self.matrix; __mul__ allows you to use the minus
        sign for subtracting two matrices.'''
    def __mul__(self, matrix2):
        answer = self.construct()
        for i in range(len(self.matrix)):
            for j in range(len(matrix2.matrix[0])):
                total = 0
                for k in range(len(self.matrix[0])):
                    total += self.matrix[i][k] * matrix2.matrix[k][j]
                answer[i][j] = total
        return answer

    
