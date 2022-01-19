# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open("task-5-3.txt", encoding="utf-8") as file_data:
    file = file_data.readlines()
    count_line = len(file)
    all_salary = 0
    average_salary = 0
    print("Сотрудники имеет оклад менее 20 тысяч >>> ")
    for line in file:
        line = line.replace("\n","")
        line = line.split(" ")
        line[1] = float(line[1])
        if line[1] < 20000:
            print(line[0])
        all_salary += line[1]
    average_salary = all_salary / count_line
    print(f"Средняя велечина дохода сотрудника {average_salary}")