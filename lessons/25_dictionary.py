# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

# ==================================
#         Dictionary Basics
# ==================================

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

# +------------------------------+
# |     Dictionary Functions    |
# +------------------------------+

capitals.get("USA") # Get the value of the USA key | Output: Washington D.C
capitals.update({"Germany":"Berlin"}) # Append or update a key and the value

capitals.pop("China") # Deletes China
capitals.popitem() # Deletes the last one
capitals.clear() # Clears the Dictionary

capitals.keys() # Returns all keys as an Object
capitals.items() # Returns all items as a dictionary Object which resembles a 2d List of Tuples

print(help(capitals)) # Prints all functions of dictionary's

# +------------------------------+
# |             Loops            |
# +------------------------------+
for value in capitals.values():
    print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")


