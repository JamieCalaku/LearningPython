# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up")
