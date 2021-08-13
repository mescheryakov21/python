class Matrix:
    def __init__(self, list_list):
        self.list_list = list_list

    def __str__(self):
        for el in self.list_list:
            print(*el, sep= ' ')
        return f'Это вид Матрица {self.list_list} '

    def __add__(self, other):
        i = 0
        new_matrix = []
        time_matrix = []
        while i < 3:
            for el_1, el_2 in zip(self.list_list[i], other.list_list[i]):
                el_sum = int(el_1) + int(el_2)
                time_matrix.append(el_sum)
            tuple(time_matrix)
            new_matrix.append(time_matrix)
            time_matrix = []
            i += 1
        return new_matrix

one_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, -1]])
print(one_matrix)
too_matrix = Matrix([[3, 2, 4], [2, -2, 8], [-9, 0, 4]])
print(too_matrix)
a = one_matrix + too_matrix
sum_matrix = Matrix(a)
print(sum_matrix)

