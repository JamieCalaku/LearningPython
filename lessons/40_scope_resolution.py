# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in


# Functions can't see inside other functions

def func1():
    a = 1
    print(b)

def func2():
    b = 2
    print(a)

#########################################################################################################

# Functions first look at local declarations if there are none they look for enclosed declarations

def func1():
    x = 1
    def func2():
        print(x) # Output: 1
    func2()

#########################################################################################################

# Global variables
y = 3

def func1():
    print(y)

def func2():
    print(y)

#########################################################################################################

# Built-In variables
from math import e

def func1():
    print(e)













func1()
func2()