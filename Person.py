class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other_obj):
        h = self.age + other_obj.age
        return Person(self.name, h)

    def __sub__(self, other_obj):
        h = self.age - other_obj.age
        return Person(self.name, h)

    def __mul__(self, other_obj):
        h = self.age * other_obj.age
        return Person(self.name, h)

    def __truediv__(self, other_obj):
        h = self.age / other_obj.age
        return Person(self.name, h)
        
p1 = Person("Alex", 15)
p2 = Person("Pesho", 15)