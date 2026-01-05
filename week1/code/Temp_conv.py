def display_menu():
    while True:
        print("Please select the temperature converter you would like to use.")
        try:
            menu = int(
                input("1. Celsius to Fahrenheit \n" "2. Fahrenheit to Celsius\n")
            )
            print(
                "------------------------------------------------------------------------"
            )
            if menu in [1, 2]:
                return menu
            else:
                print("Invalid choice ! Please enter 1 or 2.\n")
        except ValueError:
            print("Invalid Input ! Please enter a Number")


def inputfromuser():
    temperature = float(input("Please enter the value of temperature: "))
    print("------------------------------------------------------------------------")
    return temperature


def c_to_f():
    C = inputfromuser()
    F = (C * (9 / 5)) + 32
    print(f"The Celsius is {C} and the converted Fahrenheit is {F:.2f}")
    print("------------------------------------------------------------------------")


def f_to_c():
    F = inputfromuser()
    C = (F - 32) * 5 / 9
    print(f"The Fahrenheit is {F} and the converted Celsius is {C:.2f}")
    print("------------------------------------------------------------------------")


def conversion():
    choice = display_menu()

    if choice == 1:
        # Celsius → Fahrenheit
        c_to_f()

    elif choice == 2:
        # Fahrenheit → Celsius
        f_to_c()

    else:
        print("Invalid choice")


def main():
    continuation = "y"
    while continuation.lower() == "y":
        conversion()
        continuation = input("Do you want to continue? (y/n): ")


if __name__ == "__main__":
    main()
