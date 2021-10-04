def is_prime(number):
    
    return [new_list.append(each_num) for each_num in range(1, number+1) if number % each_num == 0]

number = int(input("Podaj liczbe: "))
new_list = []

is_prime(number)

if len(new_list) <= 2:
    print("Prime num!")
else:
    print("To nie jset liczba pierwsza")
