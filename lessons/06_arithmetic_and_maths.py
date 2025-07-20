import math


# +------------------------------+
# |Augmented Assignment Operators|
# +------------------------------+
# These operators combine a math operation with assignment.
# They make your code shorter and easier to read.

friends = 0

# Instead of writing:
# friends = friends + 1
# You can write:
friends += 1

# Subtraction:
friends -= 1

# Multiplication:
friends *= 3

# Division:
friends /= 2

# Exponentiation:
friends **= 2

# Modulo (remainder of division):
remainder = friends % 2





# +------------------------------+
# |         Math functions      |
# +------------------------------+

x = 3.14
y = 4
z = 5

# round function
round(x) # Output: 3.0
# if you want to round to the last 2 digits
round(23.488333, 2) # Output: 23.49


# round float up
print(math.ceil(1.2)) # Output: 2

# round float down
print(math.floor(1.8)) # Output: 1

# absolute function (value from 0)
abs(y) # Output: 4

# pow function
pow(4, 3) # Output: 64 (4 * 4 * 4)

# max value function
max(x, y, z) # Output: 5

# min value function
min(x, y, z) # Output: 3.14

########----Here are math functions you don't need often----########

# pi function
print(math.pi) # Output: 3.141592653589793

# square root function
print(math.sqrt(5)) # Output: 2.23606797749979

























