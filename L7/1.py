class Matrix:
    def __init__(self, list_in_list):
        self.list_in_list = list_in_list

    def __str__(self):
        str_end = ''
        for line in self.list_in_list:
            str_end += ' '.join(map(str, line)) + '\n'
        return str_end

    def __add__(self, other):
        if len(self.list_in_list) == len(other.list_in_list):
            for i in range(len(self.list_in_list)):
                for j in range(len(other.list_in_list[i])):
                    self.list_in_list[i][j] = self.list_in_list[i][j] + other.list_in_list[i][j]
        else:
            return f'не подходящий размер матрицы'
        return Matrix(self.list_in_list)


list1 = Matrix([[1, 1, 2], [2, 3, 3], [4, 4, 5]])
list2 = Matrix([[0, 1, 1], [2, 2, 3], [3, 4, 4]])
list3 = Matrix([[1, 2], [4, 5]])
print(list1 + list2)
print(list1 + list3)
