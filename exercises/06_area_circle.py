import math

# Exercise 2 of lesson 06
# The task is to calculate the area of a circle based on the radius

radius = float(input("Enter the radius: "))
area = math.pi * radius ** 2

print(f"The area of the circle is {round(area, 2)}cm²")
