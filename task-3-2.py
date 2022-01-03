# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(first_name, last_name, birth_year, tower, email, phone):
    """Инфорация о пользователи"""
    print(f"{first_name} {last_name} {birth_year} {tower} {email} {phone}")

user_data(first_name="Илья", last_name="Трахтынберг", birth_year=1980, tower="Моска", email="lol.maol.ru", phone="+76665554433")

