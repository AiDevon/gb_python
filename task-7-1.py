# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, arg_list: list):
        self._arg_list = arg_list

    def __str__(self):
        result_str = ""
        for line in self._arg_list:
            for col in line:
                result_str += f"{col}    "
            result_str += "\n"
        return result_str

    def __add__(self, other):
        try:
            line_count = len(self._arg_list)
            column_count = len(self._arg_list[0])
            result_list = []
            for line in range(0,line_count):
                temp_line = []
                for column in range(0,column_count):
                    temp_line.append(self._arg_list[line][column] + other._arg_list[line][column])
                result_list.append(temp_line)
            return Matrix(result_list)
        except:
            print("Не верные данные")

matrix_one = Matrix([[1, 2],
                  [3, 4],
                  [5, 6]])

matrix_two = Matrix([[7, 8],
                  [9, 10],
                  [11, 12]])

matrix_tree = matrix_one + matrix_two
print(matrix_tree)
