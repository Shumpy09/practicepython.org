import random
a = [1, 1, 2, 3, 5, 8, 10, 11, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#print([num2 for num1 in set(a) for num2 in set(b) if num1 == num2])
print([num for num in set(a) if num in b])