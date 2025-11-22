def getuserdetails():
    Name = input("Enter your name: ")
    Age = input("Enter your Age: ")
    Language = input("Enter your Language: ")
    return Name, Age, Language

def greetuser(Name,Age,Language):
    print("-----------------------------")
    print(f"Hello {Name}! 👋 \nYou are {Age} years old. \nYou're Favourite Language is {Language}.\nHave a great Day! ✨")
    print("-----------------------------")

def main():
    Name, Age, Language = getuserdetails()
    greetuser(Name, Age, Language)

if __name__ == "__main__":
    main()