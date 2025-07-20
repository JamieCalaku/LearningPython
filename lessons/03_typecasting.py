# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Jamie"
age = 14
gpa = 3.2
is_student = True

#*note* this will be False if there are no characters in the string, otherwise it will be True
name = bool(name)
age = float(age)
gpa = int(gpa)
is_student = str(is_student)

print(name) # Output: True
print(age) # Output: 14.0
print(gpa) # Output: 3
print(is_student) # Output: True (as a String)
