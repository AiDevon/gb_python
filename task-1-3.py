#Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

count = input("Введите число n: ")
count_n = int(count)
count_nn = int(count + count)
count_nnn = int(count + count + count)
sum_count = count_n + count_nn + count_nnn
print(f"Cумма {count_n} + {count_nn} + {count_nnn} = {sum_count}")
