# +------------------------------+
# |       Create 2D List        |
# +------------------------------+
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

''' or:
groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]
'''


# +------------------------------+
# |         Use 2D List         |
# +------------------------------+

print(groceries) # Output:
# [['apple', 'orange', 'banana', 'coconut'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]


print(groceries[0]) # Output:
# ['apple', 'orange', 'banana', 'coconut']


print(groceries[0][0]) # Output:
# apple


# +------------------------------+
# |      use nested loops       |
# +------------------------------+

for collection in groceries:
    for food in collection:
        print(food)

'''
Output:

apple
orange
banana
coconut
celery
carrots
potatoes
chicken
fish
turkey
'''