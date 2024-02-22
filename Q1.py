class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
all_student=[]
def new_student():
    name=input("Enter the name")
    age=int(input("Enter the age"))
    grade=int(input("enter the grade"))
    student = Student(name, age, grade)
    all_student.append(student)
    print(f"Student {student.name} is sucessfully added")
def display():
    print("List of all student")
    count=1
    for student in all_student:
            print(count ,".",student.name)
            count +=1
def total():
    print(len(all_student))

while True:
    print("Option")
    print("1.Add Student")
    print("2.Dislpay all student in the class")
    print("3.Total number of student")
    print("4.Exit")
    user_choice=int(input("Enter the choice from menu"))

    if user_choice==1:
        new_student()
    elif user_choice==2:
        display()
    elif user_choice==3:
        total()
    elif user_choice==4:
        print("Exiting the program...")
        break
    else:
         print("Invalid choice! ")