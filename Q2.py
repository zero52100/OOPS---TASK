class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

name = input("Enter the name: ")
age = int(input("Enter the age: "))
grade = int(input("Enter the grade: "))
student = Student(name, age, grade)

print("Class Name: ",type(student).__name__)
print("Student Name: ",(student.name))
print("Student Age: ",(student.age))
print("Student Grade: ",(student.grade))