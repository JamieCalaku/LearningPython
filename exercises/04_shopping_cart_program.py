# Exercise 2 from lesson 04
# The Task is to calculate the total of all products

item = input("What would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many items would you like?: "))
total = price * quantity

print(f"You have bought {quantity}x  {item}/s")
print(f"Total cost is ${total}")