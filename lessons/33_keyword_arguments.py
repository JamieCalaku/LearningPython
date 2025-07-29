# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. ARBITRARY


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# Using keyword arguments lets me ignore the order — names match the values.
hello(title="Mr.", greeting="Hello", last="Calaku", first="Jamie")