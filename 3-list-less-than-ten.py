a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_a = []

for num in a:
    if num < 5:
        new_a.append(num)
        print(num)

print(new_a)

x = [num for num in a if num < 5]
print(x)

number = int(input("Podaj liczbe: "))
y = [nums for nums in a if nums < number]
print(y)