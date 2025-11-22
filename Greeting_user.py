"""A program that takes user details and prints a nicely formatted greeting.
This teaches:
✔ input
✔ string formatting (f-strings)
✔ simple logic
✔ clean output styling"""


Name = input("Enter your name: ")
Age = input("Enter your Age: ")
Language = input("Enter your Language: ")

print("-----------------------------")
print(f"Hello {Name}! 👋 \nYou are {Age} years old. \nYou're Favourite Language is {Language}.\nHave a great Day! ✨")
print("-----------------------------")

