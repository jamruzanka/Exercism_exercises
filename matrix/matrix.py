import pandas
from pandas import DataFrame,Series

class Matrix(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def matrix_to_lines(self):
        lines = self.matrix.split("\n")
        list_of_lines = []
        for line in lines:
            line = [x for x in line if x.isdigit()]
            list_of_lines.append(line)
        return list_of_lines

    def column(self, index):
        list_of_lines = self.matrix_to_lines()
        dframe = DataFrame(list_of_lines)
        col_joined = ' '.join(dframe[index-1])
        return f"Col number {index}: " + col_joined

    def row(self, index):
        list_of_lines = self.matrix_to_lines()
        dframe = DataFrame(list_of_lines)
        row_list = []
        for i in dframe:
            row_list.append(dframe[i][index-1])
            row_joined = ' '.join(row_list)
        return f"Row number {index}: " + row_joined

    def __str__(self):
        return f"This matrix is: {self.matrix_to_lines()}"

matrix_1 = Matrix('9 6 4 \n8 3 6 \n9 3 1')
print(matrix_1)
print(matrix_1.column(3))
print(matrix_1.row(1))
