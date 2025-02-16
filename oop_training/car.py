from vehicle import Vehicle


class Car(Vehicle):
    # top_speed = 100
    # __warnings = []
    def brag(self):
        print("Look how cool my car is!")


car = Car()
car.drive()
car.add_warning("wrong way")
# car.__warnings.append("New warning")

print(car.__dict__)
print(car)
print(car.get_warnings())

car2 = Car(200)
car2.drive()
print(car2.get_warnings())

car3 = Car(250)
car3.drive()
print(car3.get_warnings())
