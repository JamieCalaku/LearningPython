# logical operators = evaluate multiple conditions (or, and, not)
#                    or  = at least one condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (not False, not True)


temp = 25
is_raining = False
is_sunny = True


# +------------------------------+
# |         Or Operator         |
# +------------------------------+

# If one of these conditions is true, the outdoor event will be canceled
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still scheduled")



# +------------------------------+
# |         And Operator        |
# +------------------------------+

# Both conditions must be true
if temp >= 28 and is_sunny:
    print("It's HOT outside 🔥️")
    print("It's SUNNY ☀️️")
elif temp <= 0 and is_sunny:
    print("It's Cold outside 🧊️")
    print("It's SUNNY ☀️️")
elif 29 > temp > 0 and is_sunny:
    print("It's WARM outside 🌤️")
    print("It's SUNNY ☀️️")




# +------------------------------+
# |         Not Operator        |
# +------------------------------+

if temp >= 28 and not is_sunny:
    print("It's HOT outside 🔥️")
    print("It's CLOUDY ☁️")
elif temp <= 0 and not is_sunny:
    print("It's COLD outside 🧊️")
    print("It's CLOUDY ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It's WARM outside 🌤️")
    print("It's CLOUDY ☁️")