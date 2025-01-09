def is_fibonacci(num):
    if num < 0:
        return False

    a = 0
    b = 1

    while a <= num:
        if a == num:
            return True
        a = a + b
        b = b + a

    return False

numero = int(input("Informe um número: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")