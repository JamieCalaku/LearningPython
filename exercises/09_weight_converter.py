# Exercise 1 from lesson 09
# The task is to convert kg in lb or lb in kg

weight = float(input("Enter the weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit.capitalize() == "K":
    print(f"{weight}kgs are {weight * 2.205} lbs.")

elif unit.capitalize() == "L":
    print(f"{weight}lbs is {weight / 2.205} kgs.")
else:
    print(f"{unit} is not valid")