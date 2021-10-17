"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*list):
    res= []
    for elem in list:
        res.append(elem * elem)
    return res
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    d = 2
    while num % d != 0:
        d += 1
    return d == num

def filter_numbers(numbers,type):
    for elem in numbers[:]:
        if type == EVEN:
                if elem % 2 != 0:
                numbers.remove(elem)
        return numbers
#     """
#     функция, которая на вход принимает список из целых чисел,
#     и возвращает только чётные/нечётные/простые числа
#     (выбор производится передачей дополнительного аргумента)
#
#     >>> filter_numbers([1, 2, 3], ODD)
#     <<< [1, 3]
#     >>> filter_numbers([2, 3, 4, 5], EVEN)
#     <<< [2, 4]
#     """
