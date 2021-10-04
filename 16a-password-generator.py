import random
import string

def passGen(b):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    numbers = string.digits

    all_of_it = upper + lower + special + numbers
    password = random.sample(all_of_it, b)
    random.shuffle(password)
    for i in password:
        password = ''.join(password)
    return password


a = int(input("How long your password would be: "))
print(f"Your password: {passGen(a)}")