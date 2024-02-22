class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade=self.cal_grade()
    def cal_grade(self):
        if self.score>90:
            print("A+")
        elif self.score>=80 and self.score<90:
            print("A")
        elif self.score>=70 and self.score<80:
            print("B+")
        elif self.score>=60 and self.score<70:
            print("B")
        elif self.score>=50 and self.score<60:
            print("C+")
        elif self.score>=40 and self.score<50:
            print("C")
        else:
            print("Failed")

    def display(self):
        print("Name:", self.name)
        print("Score:", self.score)
        print("Score:", self.grade)

name1 = input("Enter the first student name: ")
score1 = int(input(f"Enter the {name1}'s score: "))
name2 = input("Enter the second student name: ")
score2 = int(input(f"Enter the {name2}'s score: "))

student1 = Student(name1, score1)
student2 = Student(name2, score2)

print("Student 1 details:")
student1.display()

print("\nStudent 2 details:")
student2.display()
