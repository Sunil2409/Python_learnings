import random
import string

def password_generator(Length):
    if Length<8:
        return "Password should be greater than 8 digits"
        

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols


    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=Length - 4)
    random.shuffle(password)
    return ''.join(password)

Length = int(input("Enter desired length of the password: "))
print("Generated password is: ", password_generator(Length))