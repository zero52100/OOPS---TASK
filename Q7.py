class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = self.cal_grade()

    def cal_grade(self):
        if self.score > 90:
            return "A+"
        elif 80 <= self.score < 90:
            return "A"
        elif 70 <= self.score < 80:
            return "B+"
        elif 60 <= self.score < 70:
            return "B"
        elif 50 <= self.score < 60:
            return "C+"
        elif 40 <= self.score < 50:
            return "C"
        else:
            return "Failed"

    def display(self):
        print("Name:", self.name)
        print("Score:", self.score)
        print("Grade:", self.grade)
    def as_dict(self):
        return{'Name':self.name,'Score':self.score,'Grade':self.grade}

def score_input(name):
    while True:
        try:
            score = int(input(f"Enter {name}'s score: "))
            return score
        except ValueError:
            print("Invalid input. Please enter a valid integer score.")

name1 = input("Enter the first student name: ")
score1 = score_input(name1)

name2 = input("Enter the second student name: ")
score2 = score_input(name2)

student1 = Student(name1, score1)
student2 = Student(name2, score2)

print("\nStudent 1 details:")
student1.display()

print("\nStudent 2 details:")
student2.display()
print("\nUsing dictionary")
print("\nStudent 1 details using as_dict:")
print(student1.as_dict())

print("\nStudent 2 details:")
print(student2.as_dict())
