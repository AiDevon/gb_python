# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroExecp(ZeroDivisionError):
    def __str__(self):
        return f"Деление на ноль запрещено"

def FunDel(a,b):
    if b == 0:
        raise ZeroExecp
    else:
        return a/b

try:
    FunDel(100,0)
except ZeroExecp as ex:
    print(ex)