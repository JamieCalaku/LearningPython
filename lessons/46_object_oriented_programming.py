# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


    def drive(self):
        print(f"Driving {self.model}")

    def stop(self):
        print(f"Stopping {self.model}")


# Creating Objects
car1 = Car("Mustang", 2025, "Blue", False)
car2 = Car("Corvette", 2025, "Red", True)
car3 = Car("BMW", 2025, "Black", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print()

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print()

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)



print()
print()

car1.drive()
car2.drive()