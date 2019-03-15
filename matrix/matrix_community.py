class Matrix:
	def __init__(self, numbers):
		self.rows = [[i for i in row.split()] for row in numbers.split("\n")]
		self.columns = [list(l) for l in zip(*self.rows)]

matrix_1 = Matrix('9 6 4 \n8 3 6 \n9 3 1')
print(matrix_1.rows)
print(matrix_1.columns)
