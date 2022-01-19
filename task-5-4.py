# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("task-5-4-ENG.txt") as file_ENG:
    line_RUS = ""
    for line in file_ENG:
        if "One" in line:
            line = line.replace("One","Один")
        elif "Two" in line:
            line = line.replace("Two", "Два")
        elif "Three" in line:
            line = line.replace("Three", "Три")
        elif "Four" in line:
            line = line.replace("Four", "Четыре")
        line_RUS += line

with open("task-5-4-RUS.txt","w",encoding="utf-8") as file_RUS:
    file_RUS.write(line_RUS)

print(line_RUS)