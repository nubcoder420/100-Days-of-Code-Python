

def add(*args):
    return sum(args)

add(1,1,1,1,1,1,1,1,1,4,2,5,6,7,3,4,7)


class Car:
    def __init__(self, **kw):

        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(model="Skyline", make="Nissan", color="Blue")

print(my_car.make)
print(my_car.model)
print(my_car.seats)
