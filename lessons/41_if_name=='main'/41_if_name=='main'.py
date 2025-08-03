# if __name__ == '__ main __': (this script can be imported OR run standalone)
#                               Functions and classes in this module can be reused
#                               without the main block of code executing


#     ex. library = Import library for functionality
#                   When running library directly, display a help page

# This is script 2
# Script 1 is named script1_41.py

from script1_41 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script 2")
    favorite_food("sushi")
    favorite_drink("Coca Cola")
    print("Goodbye")

if __name__ == "__main__":
    main()