# Python reading files (.txt, .json)

import json

file_path_txt = "input.txt"
file_path_json = "input.json"


# DIFFERENT MODES:
# mode (r) reads the file

# Read a text file
try:
    with open(file_path_txt, "r") as file:
        file_text = file.read()
        print(file_text)

except FileNotFoundError:
    print("That file does not exist")
except PermissionError:
    print("You do not have permission to read that file")



# Read a json file
try:
    with open(file_path_json, "r") as file:
        employee = json.load(file)
        print(employee)

except FileNotFoundError:
    print("That file does not exist")
except PermissionError:
    print("You do not have permission to read that file")