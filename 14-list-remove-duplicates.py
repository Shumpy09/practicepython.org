from random import randint

def create_list():
    num_list = []
    for i in range(20):
        num_list.append(randint(1,9))
    return num_list

def set_list(num_list):
    return list(set(num_list))

numbers = create_list()

print(f"List duplicates: {numbers}")
print(f"List without duplicates: {set_list(numbers)}")