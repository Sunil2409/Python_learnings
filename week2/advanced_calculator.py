def maximum(user):
    print("The maximum number is:", max(user))


def minimum(user):
    print("The minimum number is:", min(user))


def average(user):
    print("The average number is: ", sum(user) / len(user))


def even(user):
    eve = []
    for num in user:
        if num % 2 == 0:
            eve.append(num)
    if len(eve) == 0:
        print("There is no Even numbers.")
    else:
        print("The even numbers are: ", eve)


def odd(user):
    od = []
    for num in user:
        if num % 2 != 0:
            od.append(num)
    if len(od) == 0:
        print("There is no odd numbers.")
    else:
        print("The odd numbers are: ", od)


def duplicate(user):
    dup = []
    for i in range(len(user)):
        for j in range(i + 1, len(user)):
            if user[i] == user[j]:
                if user[i] not in dup:
                    dup.append(user[i])
    if len(dup) == 0:
        print("No Duplicates Found")
    else:
        print("The duplicate numbers are: ", dup)


def main():
    continuation = "y"
    while continuation.lower() == "y":
        user = []
        while True:
            try:
                a = int(input("How many number you'd like to enter: "))
                if a <= 0:
                    print("Enter positive number")
                    continue
                break
            except ValueError:
                print("Enter only number")
        for i in range(a):
            numbers = int(input())
            user.append(numbers)

        maximum(user)
        minimum(user)
        average(user)
        even(user)
        odd(user)
        duplicate(user)
        continuation = input("If you like to continue, press y/n: ")


if __name__ == "__main__":
    main()
