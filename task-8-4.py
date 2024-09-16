# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class Storage():
    max_count: int
    technic: list

    def __init__(self, count=0):
        self.max_count = count
        self.technic = []

    def store(self, technic: list):
        self.technic.extend(technic)

class OfficeAppliances():
    purchase_date:str
    serial_number: str
    model: str
    price: float

    def __init__(self, purchase_date: str, serial_number: str, model: str, price: float):
        self.purchase_date = purchase_date
        self.serial_number = serial_number
        self.model = model
        self.price = price

class Printer(OfficeAppliances):
    type_print: str

    def __init__(self, purchase_date: str, serial_number: str, model: str, price: float,type_print: str):
        super().__init__(purchase_date, serial_number, model, price)
        self.type_print = type_print

class Scanner(OfficeAppliances):
    type_scanner: str

    def __init__(self, purchase_date: str, serial_number: str, model: str, price: float,type_scanner: str):
        super().__init__(purchase_date, serial_number, model, price)
        self.type_print = type_scanner

class Xerox(OfficeAppliances):
    type_xerox: str

    def __init__(self, purchase_date: str, serial_number: str, model: str, price: float,type_xerox: str):
        super().__init__(purchase_date, serial_number, model, price)
        self.type_print = type_xerox