number = int(input("Podaj liczbe: "))

divisors = [div for div in range(1,number+1) if number % div == 0]
print(f"Divisors of {number}: {divisors}")