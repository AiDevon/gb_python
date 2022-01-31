# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes:
    _name: str
    def __init__(self, name):
        self._name = name

class Coat(Clothes):
    _size: int
    def __init__(self,name,size):
        super().__init__(name)
        self._size = size

    @property
    def fabric_consumption(self):
        v = self._size/6.5 + 0.5
        print(f"Расход ткани у пальто модель '{self._name}' = {v}")

class Suit(Clothes):
    _growth: int
    def __init__(self,name,growth):
        super().__init__(name)
        self._growth = growth

    @property
    def fabric_consumption(self):
        h = 2*self._growth + 0.3
        print(f"Расход ткани у костюма модель '{self._name}'= {h}")

class CompositClothes(Clothes):
    def __init__(self, children: list):
        self.children = children

    def fabric_consumption(self):
        for item in self.children:
            item.fabric_consumption

one = Coat("one",100)
two = Suit("two",50)
# one.fabric_consumption
# two.fabric_consumption

one_two = CompositClothes([one, two])
one_two.fabric_consumption()