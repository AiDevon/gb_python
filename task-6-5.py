# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки»")

class Pen(Stationery):
    def draw(self):
        print("Запуск начертания")

class Pencil(Stationery):
    def draw(self):
        print("Запуск каляканья")

class Handle(Stationery):
    def draw(self):
        print("Запуск заполнения")

pen1 = Pen("ручка")
pen1.draw()

pen1 = Pencil("карандаш")
pen1.draw()

pen1 = Handle("маркер")
pen1.draw()