def div():
    try:
        Num1 = int(input("Enter Number1: "))
        Num2 = int(input("Enter Number2: "))
        result = Num1 / Num2
    except ValueError:
        print("Enter only Number")
    except ZeroDivisionError:
        print("Enter only positive number")
    else:
        return result
    finally:
        print("Please verify the output.")


div()
