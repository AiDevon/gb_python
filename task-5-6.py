# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("task-5-6.txt", encoding="utf-8") as file_data:
    subject_dict ={}
    for line in file_data:
        subject = line[:line.find(":")]

        l_index = line.find("(л)")
        if l_index != -1:
            lectures = line[l_index-3:l_index]
        else:
            lectures = 0

        p_index = line.find("(пр)")
        if p_index != -1:
           practical = line[p_index-3:p_index]
        else:
            practical = 0

        lec_index = line.find("(лаб)")
        if lec_index != -1:
            laboratory = line[lec_index-3:lec_index]
        else:
            laboratory = 0

        sum_subject = int(lectures) + int(practical) + int(laboratory)
        subject_dict[subject] = sum_subject

    print(subject_dict)