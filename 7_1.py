class Matrix:
    def __init__(self, my_matrix):
        self.matrix = my_matrix

    def __str__(self):
        output = ""
        for line in self.matrix:
            output += " ".join(map(str, line)) + "\n"
        return output

    def __add__(self, another_matrix):
        try:
            val = [[self.matrix[i][j] + another_matrix.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
            output = ""
            for line in val:
                output += " ".join(map(str, line)) + "\n"
            return output
        except IndexError:
            return "Ошибка сложения матриц: матрицы должны быть равновеликие"


my_matrix_1 = Matrix([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
my_matrix_2 = Matrix([[11, 12, 13], [12, 13, 14], [13, 14, 15]])
my_matrix_3 = Matrix([[1, 2, 3, 4], [2, 3, 4], [3, 4, 5], [4, 5, 6]])

print(my_matrix_1)
print(my_matrix_1 + my_matrix_2)
print(my_matrix_3 + my_matrix_1)
