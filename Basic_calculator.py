def inputforoperation():
    
    print("Enter the operation you would like to perform: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
    print("--------------------------------------------")
    Menu = int(input())
    print("-------------------")
    return Menu

def calcultion():
    choice = inputforoperation()
    if choice == 1:
        #Addition
        A = int(input("Enter the value of 1st Number: "))
        B = int(input("Enter the value of 2nd Number: "))
        print("--------------------------------------------")
        print(f"Addition of {A} and {B} is:", A+B)
        print("--------------------------------------------")

    if choice == 2:
        #Subtraction
        A = int(input("Enter the value of 1st Number: "))
        B = int(input("Enter the value of 2nd Number: "))
        print("--------------------------------------------")
        print(f"Addition of {A} and {B} is:", A-B)
        print("--------------------------------------------")

    if choice == 3:
        #Mulitplication
        A = int(input("Enter the value of 1st Number: "))
        B = int(input("Enter the value of 2nd Number: "))
        print("--------------------------------------------")
        print(f"Addition of {A} and {B} is:", A*B)
        print("--------------------------------------------")

    if choice == 4:
        #Division
        A = int(input("Enter the value of 1st Number: "))
        B = int(input("Enter the value of 2nd Number: "))
        print("--------------------------------------------")
        print(f"Addition of {A} and {B} is:", A/B)
        print("--------------------------------------------")

user = input("If you want to calculate something press 'y' Else type anyother Keys: ")
while user.lower() == 'y':
    calcultion()
    user = input("If you want to calculate something press 'y' Else type anyother Keys: ")

