# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.


# count to 10 (prints 1 to 10 in the console)
for x in range(1, 11):
    print(x)

# reversed count to 1 (prints 10 to 1 in the console)
for x in reversed(range(1, 11)):
    print(x)

# count to 10 with 3 steps(prints every third digit)
for x in range(1, 11, 3):
    print(x)



# +------------------------------+
# |          Examples           |
# +------------------------------+

# prints the card number one by one
credit_number = "1234-5678-9012-3456"
for x in credit_number:
    print(x)


# skips unlucky number 13 (prints all numbers from 1-20 except 13)
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)