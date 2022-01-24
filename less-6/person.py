class HumanClass:
    age: int
    first_name: str
    last_name: str
    weight: int
    _password: str
    __bank_account: str

    counter: int = 0

    def __init__(self, first_name, last_name, age, weight=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.__bank_account = "100500"

        HumanClass.counter += 1


    def info(self):
        print(f"I'm {self.first_name}, age: {self.age}, weight: {self.weight}")

    def _init_password(self):
        self._password = "11223344"

    def show_bank_account(self):
        print(f"Account: {self.__bank_account[:3]}*****")

john = HumanClass("John","Doe", 30)
artur = HumanClass("Artur","Doe", 40)

#print(johm, artur)

# johm.age = 30
# johm.first_name = "John"
# johm.last_name = "Doe"
#
# artur.age = 40
# artur.first_name = "Artur"
# artur.last_name = "Doe"
#
john.info()
artur.info()

print(john.counter)
print((artur.counter))

john._init_password()
print(john._password)

john.show_bank_account()

#print(john._HumanClass__bank_account)