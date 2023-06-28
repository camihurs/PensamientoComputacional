import time
import sys

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 10000
    sys.setrecursionlimit(n + 10)

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f"Execution time with bucle\t{final - comienzo}")


    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(f"Execution time with recursive\t{final - comienzo}")