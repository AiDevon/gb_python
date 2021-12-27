# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

input_number = int(input("Введите месяц в виде целого числа от 1 до 12 >>> "))

# Решение через список
month_list = ['январь', 'февраль', 'март', 'апрель',
              'май', 'июнь', 'июль', 'август',
              'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

if input_number == 12 or input_number == 1 or input_number == 2:
    print(f"Месяц {month_list[input_number - 1]} относится к зиме")
elif input_number == 3 or input_number == 4 or input_number == 5:
    print(f"Месяц {month_list[input_number - 1]} относится к весне")
elif input_number == 6 or input_number == 7 or input_number == 8:
    print(f"Месяц {month_list[input_number - 1]} относится к лету")
elif input_number == 9 or input_number == 10 or input_number == 11:
    print(f"Месяц {month_list[input_number - 1]} относится к осине")
