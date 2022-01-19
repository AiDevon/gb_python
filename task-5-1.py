# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

file = open("task-5-1.txt","w")

while True:
    input_sting = input("Введите данные >>> ")
    if input_sting == "":
        break
    else:
        file.write(input_sting + "\n")

file.close()