# Exercise 1 from lesson 34

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Jamie", "Calaku", "III",
               street="123 Fake St.",
               city="San Francisco",
               state="California",
               zip="94035")