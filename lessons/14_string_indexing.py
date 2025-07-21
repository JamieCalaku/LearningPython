# +------------------------------+
# |       String Indexing       |
# +------------------------------+

# indexing = accessing elements of a sequence using [] (indexing operator)
# format: [start : end : step]

credit_number = "1234-5678-9012-3456"

# +------------------------------+
# |  Accessing Single Characters |
# +------------------------------+

# get the 5th character (index 4 because indexing starts at 0)
print(credit_number[4])  # Output: -

# get the last character
print(credit_number[-1])  # Output: 6

# get the 3rd character from the end
print(credit_number[-3])  # Output: 4

# +------------------------------+
# |       Accessing Slices       |
# +------------------------------+

# get all characters from index 0 to 3 (4 is excluded)
print(credit_number[0:4])  # Output: 1234

# get all characters from index 5 to the end
print(credit_number[5:])  # Output: 5678-9012-3456

# get the full string with every 2nd character
print(credit_number[::2])  # Output: 13-6891-46