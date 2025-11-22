def menu():
    print("Please select the temperature converter you would like to use.")
    Menu = int(input("1. Celsius to Fahrenheit \n" "2. Fahrenheit to Celsius\n"))
    print("------------------------------------------------------------------------")
    return Menu

def inputfromuser():
    temperature = float(input("Please enter the value of temperature: "))
    print("------------------------------------------------------------------------")
    return temperature

def conversion():
    choice = menu()
    if choice == 1:
        #Celsius → Fahrenheit
        C = inputfromuser()
        F = (C * (9/5)) + 32
        print(f"The Celsius is {C} and the converted Fahrenheit is {F:.2f}")
        print("------------------------------------------------------------------------")

    if choice == 2:
        #Fahrenheit → Celsius
        F = inputfromuser()
        C = (F - 32) * 5/9
        print(f"The Fahrenheit is {F} and the converted Celsius is {C:.2f}")
        print("------------------------------------------------------------------------")

conversion()



