# format specifiers = {value:flags} format a value based on what
#                                   flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number)f = allocate that many spaces
# :03 = allocate that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


# +------------------------------+
# |      Format Specifiers      |
# +------------------------------+

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# +------------------------------+
# |  .(number)f = Fixed decimals |
# +------------------------------+

# Round to 2 decimal places
print(f"Price 1 is ${price1:.2f}")
# Output: Price 1 is $3.14

# +------------------------------+
# |  :(number)f = Field width    |
# +------------------------------+

# Allocate 10 spaces, right-aligned by default
print(f"Price 1 is ${price1:10.2f}")
# Output: Price 1 is $      3.14

# +------------------------------+
# |  :03 = Zero-padding width    |
# +------------------------------+

# Minimum width 3, padded with zeros
num = 5
print(f"Number: {num:03}")
# Output: Number: 005

# +------------------------------+
# |  :< = Left align             |
# +------------------------------+

print(f"Left:  |{price3:<10.2f}|")
# Output: Left:  |12.34     |

# +------------------------------+
# |  :> = Right align            |
# +------------------------------+

print(f"Right: |{price3:>10.2f}|")
# Output: Right: |     12.34|

# +------------------------------+
# |  :^ = Center align           |
# +------------------------------+

print(f"Center:|{price3:^10.2f}|")
# Output: Center:|  12.34   |

# +------------------------------+
# |  :+ = Force plus sign        |
# +------------------------------+

print(f"Signed: {price1:+.2f}")
# Output: Signed: +3.14

# +------------------------------+
# |  := = Sign before padding    |
# +------------------------------+

print(f"Force Sign Left: {price2:=10.2f}")
# Output: Force Sign Left: -   987.65

# +------------------------------+
# |  :  = Space before positives |
# +------------------------------+

print(f"Space sign: {price1: .2f}")
# Output: Space sign:  3.14

print(f"Space sign: {price2: .2f}")
# Output: Space sign: -987.65

# +------------------------------+
# |  :, = Comma separator        |
# +------------------------------+

big_number = 1234567.89
print(f"With comma: {big_number:,.2f}")
# Output: With comma: 1,234,567.89