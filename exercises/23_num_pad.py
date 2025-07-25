# Exercise 1 from lesson 23
# Task is to print a numpad in the console

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))


for row in num_pad:
    for num in row:
        print(num, end=" ")
        
    print()