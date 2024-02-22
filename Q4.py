class Staff:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

class Teacher(Staff):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Role:", self.role)
        print("Department:", self.department)

name = input("Enter the name: ")
age = int(input("Enter your age: "))
role = input("Enter your role: ")
department = input("Enter the department: ")
salary = float(input("Enter the salary: "))
teacher1 = Teacher(name=name, age=age, role=role, department=department, salary=salary)

teacher1.print_details()
