from math import sqrt


def power_numbers(*numbers):
    res = []
    for elem in numbers:
        res.append(elem * elem)
    return res


ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False


def filter_numbers(num, filter_type):
    if filter_type == EVEN:
        num = list(filter(is_even, num))
        return num
    if filter_type == ODD:
        num = list(filter(is_odd, num))
        return num
    if filter_type == PRIME:
        num = list(filter(is_prime, num))
        return num
