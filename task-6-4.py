# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self,speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self):
        print(f"{self.name} повернула")

    def show_speed(self):
        print(f"скорость {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} превышение скорости > 60")
        else:
            print(f"скорость {self.speed}")

class SportCar(Car):
     def show_color(self):
         print(f"Цвет этой спортивной машины {self.color}")

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} превышение скорости > 60")
        else:
            print(f"скорость {self.speed}")

class PoliceCar(Car):
    pass

car1 = TownCar(70,"Красный","Маруся", False)
car1.show_speed()