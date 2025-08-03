# Python file detection

import os

file_path = "test.txt"

# Checks if the path exists
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    # Checks if the path is a file or a directory
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print(f"The location '{file_path}' does not exist")