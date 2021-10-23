"""
Домашнее задание №1
Функции и структуры данных
"""
from math import sqrt


def power_numbers(*numbers):
    res = []
    for elem in numbers:
        res.append(elem * elem)
    return res
    # """
    # функция, которая принимает N целых чисел,
    # и возвращает список квадратов этих чисел
    # >>> power_numbers(1, 2, 5, 7)
    # <<< [1, 4, 25, 49]
    # """


# filter types
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


print(filter_numbers([2, 3, 4, 5, 6, 7, 8, 9, 10], ODD))

    # """
    # функция, которая на вход принимает список из целых чисел,
    # и возвращает только чётные/нечётные/простые числа
    # (выбор производится передачей дополнительного аргумента)
    #
    # >>> filter_numbers([1, 2, 3], ODD)
    # <<< [1, 3]
    # >>> filter_numbers([2, 3, 4, 5], EVEN)
    # <<< [2, 4]
    # """