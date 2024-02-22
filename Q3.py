class Square:
    def __init__(self,lenght):
        self.side_lenght=lenght
    def area(self):
        return self.side_lenght*2
    def perimeter(self):
        return self.side_lenght*4
    
lenght=float(input("Enter the leght of square"))
new_sqaure=Square(lenght)

while True:
    print("Option")
    print("1.calculate area")
    print("2.calculate perimeter")
    print("3.calculate area and perimeter")
    print("4.Exit")
    user_choice=int(input("Enter the choice from menu : "))

    if user_choice==1:
        print("Area :",new_sqaure.area())
    elif user_choice==2:
        print("Perimeter :",new_sqaure.perimeter())
    elif user_choice==3:
        print("Area :",new_sqaure.area())
        print("Perimeter :",new_sqaure.perimeter())
    elif user_choice==4:
        print("Program Exited")
        break
    else:
         print("Invalid choice! ")


    