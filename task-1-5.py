revenue = int(input("Введите выручку: "))
cost = int(input("Введите издержки: "))
result = revenue - cost
if result > 0:
    print(f"Фирма работает с прибылью {result}")
else:
    print(f"Фирма работает в убыток {result}")

count_staff = int(input("Введите количество сотрудников: "))
profit = result / count_staff
if result > 0:
    print(f"Прибыль фирмы в расчете на одного сотрудника {profit:.2f}")
else:
    print(f"Убыток фирмы в расчете на одного сотрудника {profit:.2f}")
