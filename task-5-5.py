# Создать(программно) текстовый файл, записать в него программно набор чисел,разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open("task-5-5.txt",'w') as file_data:
    input_line = input("Введите числа через пробел >>> ")
    file_data.write(input_line)

with open("task-5-5.txt") as file_data:
    line = file_data.read()
    line = line.split(" ")
    sum_line = 0
    for l in line:
        sum_line += int(l)
    print(f"Сумма чисел = {sum_line}")