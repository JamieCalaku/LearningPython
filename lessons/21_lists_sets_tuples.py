# +------------------------------+
# |         Collections          |
# +------------------------------+
# Used to store multiple values in a single variable.
# - List  = [] ordered + changeable. Duplicates OK
# - Set   = {} unordered + no duplicates. Add/remove OK
# - Tuple = () ordered + unchangeable. Duplicates OK. Faster access


# ==================================
#            List Basics
# ==================================

fruits_list = ["apple", "orange", "banana", "coconut"]

# +------------------------------+
# |       Indexing & Slicing     |
# +------------------------------+

print(fruits_list[0])     # Output: apple
print(fruits_list[1])     # Output: orange
print(fruits_list[-1])    # Output: coconut

print(fruits_list[::-1])  # Output: ['coconut', 'banana', 'orange', 'apple']
print(fruits_list[0:3])   # Output: ['apple', 'orange', 'banana']
print(fruits_list[:1])    # Output: ['apple']


# +------------------------------+
# |             Loops            |
# +------------------------------+

for fruit in fruits_list:
    print(fruit)

# +------------------------------+
# |         List Functions       |
# +------------------------------+

len(fruits_list)                # Get number of elements
"apple" in fruits_list          # Check if value exists → True/False

fruits_list[0] = "pineapple"    # Change value at index
fruits_list.append("kiwi")      # Add to end
fruits_list.remove("banana")    # Remove by value
fruits_list.insert(1, "lemon")  # Insert at index
fruits_list.sort()              # Sort alphabetically
fruits_list.reverse()           # Reverse list
fruits_list.clear()             # Remove all elements

fruits_list.index("orange")     # Get index of value
fruits_list.count("apple")      # Count occurrences






# ==================================
#            Set Basics
# ==================================

fruits_set = {"apple", "orange", "banana", "coconut"}

# +------------------------------+
# |         Set Functions        |
# +------------------------------+

len(fruits_set)                 # Number of elements
"apple" in fruits_set           # Check if value exists → True/False

fruits_set.add("kiwi")          # Add element
fruits_set.remove("kiwi")       # Remove element
fruits_set.pop()                # Remove random element
fruits_set.clear()              # Remove all elements







# ==================================
#           Tuple Basics
# ==================================

fruits_tuple = ("apple", "orange", "banana", "coconut")

# +------------------------------+
# |        Tuple Functions       |
# +------------------------------+

len(fruits_tuple)               # Number of elements
"apple" in fruits_tuple         # Check if value exists → True/False

fruits_tuple.index("orange")    # Get index of value
fruits_tuple.count("banana")    # Count occurrences