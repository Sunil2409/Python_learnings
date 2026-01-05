def inputforoperation():
    try:
        print(
            "Enter the operation you would like to perform: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
        print("--------------------------------------------")
        Menu = int(input())
        if Menu in [1, 2, 3, 4]:
            return Menu
        else:
            print("Invalid Choice! Please enter 1,2,3 or 4")
    except ValueError:
        print("Invalid Input ! Please enter a Number")
        print("----------------------------------")

def add():
    A = int(input("Enter the value of 1st Number: "))
    B = int(input("Enter the value of 2nd Number: "))
    print("--------------------------------------------")
    print(f"Addition of {A} and {B} is:", A + B)
    print("--------------------------------------------")


def sub():
    A = int(input("Enter the value of 1st Number: "))
    B = int(input("Enter the value of 2nd Number: "))
    print("--------------------------------------------")
    print(f"Subtraction of {A} and {B} is:", A - B)
    print("--------------------------------------------")


def mul():
    A = int(input("Enter the value of 1st Number: "))
    B = int(input("Enter the value of 2nd Number: "))
    print("--------------------------------------------")
    print(f"Multiplication of {A} and {B} is:", A * B)
    print("--------------------------------------------")


def div():
    A = int(input("Enter the value of 1st Number: "))
    B = int(input("Enter the value of 2nd Number: "))

    print("--------------------------------------------")
    try:
        print(f"Division of {A} and {B} is:", A / B)
    except ZeroDivisionError:
        print("You cannot divide by 0. Please enter a valid number")
    print("--------------------------------------------")


def calculation():
    choice = inputforoperation()
    if choice == 1:
        # Addition
        add()
    if choice == 2:
        # Subtraction
        sub()

    if choice == 3:
        # Mulitplication
        mul()

    if choice == 4:
        # Division
        div()

def main():
    continuation = "y"
    while continuation.lower() == "y":
        calculation()
        continuation = input("Do you want to continue? (y/n): ")


if __name__ == "__main__":
    main()
