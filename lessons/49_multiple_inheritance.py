# multiple inheritance = inherit from more than one parent class
#                        C(A, B)



# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A




# Grand parent
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")




# Parent
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")



# Children
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass



rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


# Rabbit only has the flee method (inheritance from the Prey Class)
rabbit.flee()

# Hawk only has the hunt method (inheritance from the Predator Class)
hawk.hunt()

# Fish has the flee and hunt method (inheritance from the Prey and Predator Class)
fish.flee()
fish.hunt()


# But all animals have the eat and sleep methods (inheritance from the Animal class)
rabbit.sleep()
hawk.sleep()
fish.sleep()

rabbit.eat()
hawk.eat()
fish.eat()