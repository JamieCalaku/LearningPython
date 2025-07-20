import math

# Exercise 1 of lesson 06
# The task is to calculate the circumference of a circle based on the radius


radius = float(input("Enter the radius: "))
circumference = 2 * math.pi * radius

print(f"The circumference of the circle is: {round(circumference, 2)}")