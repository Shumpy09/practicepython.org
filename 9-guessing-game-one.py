from random import randint
import sys

rand_num = randint(1,9)
guess = 0
number = 0

while number != 'exit':
    number = input("Podaj liczbe. Wpisz exit zeby przerwac: ")
    
    if number == 'exit':
        break

    if rand_num == int(number):
        print("Gratulacje, trafiles wylosowaną liczbe!")
        guess +=1
        print(f"Liczba prób: {guess}")
        
        guess = 0
        rand_num = randint(1,9)
        
    elif rand_num > int(number):
        print("Za malo")
        guess +=1
    elif rand_num < int(number):
        print("Za duzo")
        guess +=1