# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True


    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")



# Dog class inherits all attributes from the animal class
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MIAU!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")



dog = Dog("Buddy")
cat = Cat("Mexico")
mouse = Mouse("Mickey")



# You can use the attributes of the animal class
print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

# Extra methods
dog.speak()

cat.speak()

mouse.speak()
