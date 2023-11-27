# unlimited positional arguments *args
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 3, 4, 5))


# unlimited keyword arguments
def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multipy=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("4")


my_car = Car(make="Nissan")
print(my_car.model)