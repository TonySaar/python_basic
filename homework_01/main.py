from math import sqrt


def power_numbers(*numbers):
    return [elem ** 2 for elem in numbers]


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
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


filters = {
    EVEN: is_even,
    ODD: is_odd,
    PRIME: is_prime,
}


def filter_numbers(num, filter_type):
    return list(filter(filters[filter_type],num))

    # if filter_type == EVEN:
    #     num = list(filter(is_even, num))
    #     return num
    # if filter_type == ODD:
    #     num = list(filter(is_odd, num))
    #     return num
    # if filter_type == PRIME:
    #     num = list(filter(is_prime, num))
    #     return num
