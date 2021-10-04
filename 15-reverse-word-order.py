def get_string():
    user_string = str(input("Twoj napis: "))
    return user_string

def reverse_string(string):
    return ' '.join(string.split()[::-1])
    

print(reverse_string(get_string()))
