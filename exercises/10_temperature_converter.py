# Exercise 1 from lesson10
# The task is to convert Celsius in Fahrenheit or Fahrenheit in celsius

temperature = float(input("Enter the Temperature: "))
unit = input("Celsius or Fahrenheit? (C or F): ")

if unit.capitalize() == "C":
    print(f"{temperature} °C are {temperature * 1.8 + 32} °F.")

elif unit.capitalize() == "F":
    print(f"{temperature} °F are {(temperature - 32) / 1.8} °C.")
else:
    print(f"{unit} is not valid")

