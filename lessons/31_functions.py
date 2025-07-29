# function = A block of reusable code
#            place () after the function name to invoke it


# +------------------------------+
# |          Functions          |
# +------------------------------+
# Define a function
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Jamie", 10.99, "25/06/2029")



# +------------------------------+
# |             Return          |
# +------------------------------+

# Return = statement used to end a function
#          and send a result back to the caller


def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z


print(add(1, 2)) # Output: 3
print(subtract(1, 2)) # Output: -1
print(multiply(1, 2)) # Output: 2
print(divide(1, 2)) # Output: 0.5



# +------------------------------+
# |           Example           |
# +------------------------------+

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("jamie", "calaku")
print(full_name)