# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class


class Student:
    # Class variable (shared by all students)
    class_year = 2032
    num_students = 0

    def __init__(self, name, age):
        # Instance variables (unique to each student)
        self.name = name
        self.age = age
        # Increment the number of Students by 1 everytime we create a new Student Instance
        Student.num_students += 1

# Create two student objects
student1 = Student("Jamie", 14)
student2 = Student("Martin", 20)

# Print instance variables
print("Student 1:")
print(student1.name)
print(student1.age)

print()

print("Student 2:")
print(student2.name)
print(student2.age)

print()

# Print class variable
print(f"Graduation Year: {Student.class_year}")
print(f"Number of Students: {Student.num_students}")

print()

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)