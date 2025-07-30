# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop


# Lists are iterable
numbers_list = [1, 2, 3, 4, 5]
for number in numbers_list:
    print(number, end=" ")

print()

# Tuples are iterable
numbers_tuple = (1, 2, 3, 4, 5)
for number in numbers_tuple:
    print(number, end=" ")

print()

# Sets are iterable
fruits_set = {"apple", "orange", "banana", "coconut"}
for fruit in fruits_set:
    print(fruit, end=" ")

print()

# Strings are iterable
name_string = "Jamie Calaku"
for character in name_string:
    print(character, end=" ")

print()

# Dictionaries are iterable
my_dictionary = {"A": 1, "B": 2, "C": 3}
for key, value in my_dictionary.items():
    print(f"{key} = {value}")