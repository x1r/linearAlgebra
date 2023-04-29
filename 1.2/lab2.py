from copy import deepcopy
import random


class matrix(object):
    def __init__(self, rows: int, columns: int):
        self.rows: int = rows
        self.columns: int = columns
        self.matrix = []

        for i in range(rows):
            self.matrix.append([])

        for row in self.matrix:
            for i in range(columns):
                row.append(0)

    def __getitem__(self, tuple):
        row, column = tuple
        return self.matrix[row][column]

    def __setitem__(self, tuple, value):
        row, column = tuple
        self.matrix[row][column] = value

    def __repr__(self):
        string = ""
        for row in self.matrix:
            for element in row:
                string += str(element) + " "
        string = string.rstrip()
        return string

    def __contains__(self, value):
        for row in self.matrix:
            for element in row:
                if element == value:
                    return True
                else:
                    pass
        return False

    def size(self):
        rows = self.rows
        columns = self.columns
        return rows, columns

    def __str__(self):
        rows = self.rows
        columns = self.columns
        return str(rows) + " " + str(columns)

    def __add__(self, other):
        result = deepcopy(self)
        if isinstance(other, float) and self.is_square():
            for i in range(self.rows):
                result[i, i] += other
            return result
        if self.size() != other.size():
            raise Exception("Matrixes are not the same sized.\n Unable to summarize two matrixes\n")
        for s in range(self.rows):
            for c in range(self.columns):
                result[s, c] += other[s, c]
        return result

    def __sub__(self, other):
        result = deepcopy(self)
        if isinstance(other, float) and self.is_square():
            for i in range(self.rows):
                result[i, i] -= other
            return result
        if self.size() != other.size():
            raise Exception("Matrixes are not the same sized.\n Unable to summarize two matrixes\n")
        for s in range(self.rows):
            for c in range(self.columns):
                result[s, c] -= other[s, c]
        return result

    def __mul__(self, other):
        if isinstance(other, float):
            multipliedMatrix = matrix(self.rows, self.columns)
            for row in range(self.rows):
                for column in range(self.columns):
                    multipliedMatrix[row, column] = self[row, column] * other
            return multipliedMatrix
        if isinstance(other, matrix):
            if self.columns != other.rows:
                raise Exception("Matrixes can not be multiplied as their size are unsupported")
            multipliedMatrix = matrix(self.rows, other.columns)
            for row in range(self.rows):
                for column in range(other.columns):
                    element = 0
                    for sumIndex in range(self.columns):
                        element += self[row, sumIndex] * other[sumIndex, column]
                    multipliedMatrix[row, column] = element
            return multipliedMatrix

    def __rmul__(self, other):
        return self * other

    def obratnaya_matrix(self):
        if not self.is_square():
            raise Exception("Matrix is not square")
        if self.determinant() == 0:
            raise Exception("Matrix is not invertible")
        obratnayaMatrix = matrix(self.rows, self.columns)
        for row in range(self.rows):
            for column in range(self.columns):
                obratnayaMatrix[row, column] = self.cofactor(column, row) / self.determinant()
        return obratnayaMatrix

    def cofactor(self, row, column):
        return ((-1) ** (row + column)) * self.minor(row, column)

    def minor(self, row, column):
        minorMatrix = matrix(self.rows - 1, self.columns - 1)
        for i in range(self.rows):
            for j in range(self.columns):
                if i != row and j != column:
                    minorMatrix[i - int(i > row), j - int(j > column)] = self[i, j]
        return minorMatrix.determinant()

    def determinant(self):
        if not self.is_square():
            raise Exception("Matrix is not square")
        if self.rows == 1:
            return self[0, 0]
        if self.rows == 2:
            return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0]
        result = 0
        for i in range(self.columns):
            result += self[0, i] * self.cofactor(0, i)
        return result


    def __pow__(self, power, modulo=None):
        if isinstance(power, str):
            if power == "T":
                newMatrix = matrix(self.columns, self.rows)
                for row in range(self.rows):
                    for column in range(self.columns):
                        newMatrix[column, row] = self.matrix[row][column]
                return newMatrix
        poweredMatrix = deepcopy(self)
        if power >=1:
            for _ in range(power - 1):
                poweredMatrix *= self
        elif power == 0:
            poweredMatrix = matrix(self.rows, self.columns)
            for i in range(self.rows):
                poweredMatrix[i, i] = 1
        elif power == -1:
            poweredMatrix = self.obratnaya_matrix()
        return poweredMatrix

    def __truediv__(self, other):
        if isinstance(other, float):
            multipliedMatrix = matrix(self.columns, self.rows)
            for row in range(self.rows):
                for column in range(self.columns):
                    multipliedMatrix[row, column] = self[row, column] / other
            return multipliedMatrix

    def is_square(self):
        return self.rows == self.columns


def matrixMaker(characteristics: str, rawData: str) -> matrix:
    rows, columns = map(int, characteristics.split())
    splittedRawData = list(map(float, rawData.split()))
    result = matrix(rows, columns)
    i = 0
    for row in range(rows):
        for column in range(columns):
            result[row, column] = splittedRawData[i]
            i += 1
    return result


def answer(A, B, C, Alpha):
    with open("output.txt", "w") as fOut:
        if 1:
        # try:
            action1 = Alpha * B
            del Alpha
            del B
            action2 = C ** "T"
            action3 = action1 + action2
            del action1
            del action2
            result = A * action3
            del A
            del action3
            fOut.write("1.py")
            fOut.write("\n")
            fOut.write(str(result))
            fOut.write("\n")
            fOut.write(repr(result))


def main():
    with open("input.txt") as fIn:
        A = matrixMaker(fIn.readline(), fIn.readline())
        B = matrixMaker(fIn.readline(), fIn.readline())
        C = matrixMaker(fIn.readline(), fIn.readline())
        Alpha = float(fIn.readline())
        # answer(A, B, C, Alpha)
        result = -2 * (A**2) - 10*A + 2
        print(repr(result))



if __name__ == "__main__":
    main()