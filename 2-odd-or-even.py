"""number = int(input("Podaj liczbe: "))

if number % 4 == 0:
    print(f"Twoja liczba {number} jest podzielna przez 4. ")
else:
    print(f"Twoja liczba {number} nie jest podzielna przez 4")
"""

num = int(input("Podaj liczbe do sprawdzenia: "))
check = int(input("Podaj liczbe sprawdzającą: "))

if num % check == 0:
    print(f"Liczba {num} jest podzielna przez liczbe {check}")
else:
    print(f"Liczba {num} nie jest podzielna przez liczbe {check}")