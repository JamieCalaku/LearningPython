# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

# A while loop works almost like an IF-Statement except it will infinitely execute code until the condition is true
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")