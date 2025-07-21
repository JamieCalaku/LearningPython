# Exercise 1 from lesson 13
# The task is to check if a given username is valid
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

print("1. username is no more than 12 characters")
print("2. username must not contain spaces")
print("3. username must not contain digits")

username = str(input("Enter your username: "))

if len(username) > 12:
    print("Your username can't be more than 12 characters")

if not username.find(" ") == -1:
    print("Your username can't contain spaces")

if not username.isalpha():
    print("Your username can't contain numbers")


if len(username) <= 12 and username.find(" ") == -1 and username.isalpha():
    print(f"Welcome {username}")

