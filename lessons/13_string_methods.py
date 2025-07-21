# +------------------------------+
# |       String Basics         |
# +------------------------------+

name = "Jamie Calaku"

# length function (returns the number of characters)
len(name)  # Output: 12

# count function (counts occurrences of a character or substring)
name.count(" ")  # Output: 1

# +------------------------------+
# |   Searching in Strings      |
# +------------------------------+

# find function (first occurrence of a character)
name.find("a")  # Output: 1
# returns -1 if not found

# rfind function (last occurrence of a character)
name.rfind("a")  # Output: 9

# +------------------------------+
# |        Changing Case       |
# +------------------------------+

# capitalize() – capitalizes only the first letter
name.capitalize()  # Output: Jamie calaku

# upper() – converts all characters to uppercase
name.upper()  # Output: JAMIE CALAKU

# lower() – converts all characters to lowercase
name.lower()  # Output: jamie calaku

# +------------------------------+
# |   Checking String Content   |
# +------------------------------+

# isdigit() – returns True if string contains only digits
"0234".isdigit()  # Output: True
name.isdigit()    # Output: False

# isalpha() – returns True if string contains only letters
"Jamiecalaku".isalpha()      # Output: True  
"Jamie Calaku123".isalpha()  # Output: False

# +------------------------------+
# |   Modifying Strings         |
# +------------------------------+

# replace() – replaces a substring with another
name.replace(" ", "_")  # Output: Jamie_Calaku

# +------------------------------+
# |    Explore All Methods       |
# +------------------------------+

# Shows all string methods and their documentation
print(help(str))