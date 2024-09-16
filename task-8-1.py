# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class date:
    def __init__(self,data_str:str):
        self.date_string = data_str

    @staticmethod
    def date_to_int(date_string: str):
        date_list = [int(i) for i in date_string.split("-")]
        return date_list

    @classmethod
    def data_validation(cls,date_string: str):
        date_list = cls.date_to_int(date_string)
        assert 1 <= date_list[0] <= 31, "Не верные входные данные числа"
        assert 1 <= date_list[1] <= 12, "Не верные входные данные месяца"
        assert 1147 <= date_list[2] <= 2022, "Не верные входные данные год"
        print(date_list)

date.data_validation("31-12-2222")