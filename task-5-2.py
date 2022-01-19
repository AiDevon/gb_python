# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open("task-5-2.txt",encoding="utf-8") as file_data:
    count_line = 0
    file = file_data.readlines()
    print(f'Количество строк {len(file)}')
    for line in file:
        count_line += 1
        line = line.split(" ")
        print(f"В строке № {count_line} содержится {len(line)} слов")

    # count_line = 0
    # for line in file_data:
    #     count_line += 1
    # print(f'Количество строк {count_line}')