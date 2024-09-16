# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumbers():
    a: float
    b: float

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __add__(self, other: 'ComplexNumbers'):
        return ComplexNumbers(self.a + other.a, self.b + other.b)

    def __mul__(self, other: 'ComplexNumbers'):
        """ z1 * z2 = (a1*a2+b1*b2) + (a1*b2+a2*b1)i"""
        a3 = self.a * other.a - self.b * other.b
        b3 = self.a * other.b + other.a * self.b
        return ComplexNumbers(a3, b3)

    def __str__(self):
        if self.b > 0:
            return f"{self.a}+{self.b}i"
        else:
            return f"{self.a}{self.b}i"

z1 = ComplexNumbers(10,-5)
z2 = ComplexNumbers(11,6)
z3 = z1 + z2
z4 = z1 * z2
print(z3)
#print(complex(10,-5)+complex(11,6))
print(z4)
#print(complex(10,-5)*complex(11,6))
