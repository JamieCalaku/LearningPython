# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains




# +------------------------------+
# |           strings           |
# +------------------------------+

#Example of a normal String that will be printed
first_name = "Jamie"
print(first_name)

#Example of a String that will be printed as an f-String
first_name = "Jamie"
fav_food = "Sushi"
print(f"Hello, my name is {first_name}")
print(f"My favourite food is {fav_food}")



# +------------------------------+
# |           Integers          |
# +------------------------------+

#Example of a Integer that will be printed as an f-String
age = 14 #25.06.2011
print(f"I am {age} years old")



# +------------------------------+
# |           Floats            |
# +------------------------------+

#Example of a Float that will be printed as an f-String
price = 10.99
distance = 1.2
print(f"The price is ${price}")
print(f"The distance is ${distance}")



# +------------------------------+
# |           Boolean           |
# +------------------------------+

#Example of a Boolean that will be printed as an f-String
is_student = True
if is_student:
    print(f"He is a student")
else:
    print(f"He isn't a student")