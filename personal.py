class Person:
    def __init__(self, attrs: dict):
        self._attributes = attrs

    def __del__(self):
        print("Person remove")

    def __str__(self):
        return f"Person: {self._attributes['first_name']} {self._attributes['last_name']}"

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        return self._attributes[item]

    def __setattr__(self, key, value):
        if "_attributes" in self.__dict__:
            self._attributes[key] = value
        else:
            super().__setattr__(key,value)

john = Person({"first_name": "John", "last_name": "Doe", "age": 30})
artur = Person({"first_name": "Artur", "last_name": "Doe", "age": 40})

users = [john,artur]
print(users)
#del john

#print(john.attributes["first_name"])
print(john)

print(john["first_name"])