a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []
for num1 in a:
    for num2 in b:
        if num2 == num1:
            new_list.append(num2)
print(new_list)

i = [x for x in set(a) if x in set(b)]
print(i)