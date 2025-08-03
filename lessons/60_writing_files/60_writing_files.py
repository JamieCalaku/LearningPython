# Python writing files (.txt, .json)

import json


file_path_txt = "output.txt"
file_text = "Hello World"

file_path_json = "output.json"
employee = {
    "name": "Jamie",
    "age": 14,
    "job": "Software Engineer",
}

# DIFFERENT MODES:
# mode (x) only writes if there is no existing file
# mode (w) writes even if the file exists and overrides it
# mode (a) appends any new data

# Create a text file
try:
    with open(file_path_txt, "w") as file:
        file.write(file_text)
        print(f"text file '{file_path_txt}' was created")

except FileNotFoundError:
    print("That file does not exist")



# Create a json file
try:
    with open(file_path_json, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path_json}' was created")

except FileNotFoundError:
    print("That file does not exist")
