# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#             * unpacking operator
#             1. positional, 2. DEFAULT, 3. keyword, 4. ARBITRARY


# *args
def add(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))


# **kwargs
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
              city="San Francisco",
              state="California",
              zip="94035")
