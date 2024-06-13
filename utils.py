import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_power_of_5(n):
    if n < 1:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1


def is_power_of_2(n):
    if n < 1:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

