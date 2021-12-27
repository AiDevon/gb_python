# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

input_string = input("Введите список через пробел n1 n2 ...  >>> ")
input_list = input_string.split()
print(type(input_list))
print(input_list)

len_list = len(input_list) // 2
tmp_count = 0
while tmp_count <= len_list:
    input_list[tmp_count], input_list[tmp_count + 1] = input_list[tmp_count + 1], input_list[tmp_count]
    tmp_count += 2

print(input_list)
