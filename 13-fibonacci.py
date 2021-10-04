def sequence():
    seq_num = int(input("Ile sekwencji kodu ma zostać wykonana: "))
    return seq_num

def fibonacci(seq_num):
    fib1, fib2 = 1, 1
    fibo = [fib1, fib2]

    for n in range(1, seq_num+1):
        n = fib1 + fib2
        fibo.append(n)
        fib2 = fib1
        fib1 = n
    
    return fibo

print(fibonacci(sequence()))