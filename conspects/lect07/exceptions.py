# class IncorrectValueNumber(BaseException):
#     pass
#
#

# import logging

# try:
#     f = open('otus') # ранее говорили, что лучше делать открытие файла через with open
#     content = f.readlines()
#     print (content)
# except AttributeError:
#     print('file is not found')
# finally:
#     f.close()


# try:
#     with open ('otus', 'r') as file: # ранее говорили, что лучше делать открытие файла через with open
#         print (file.read())
# except FileNotFoundError as e:
#     print(e, 'file is not found')

# finally:
#     f.close()

# try:
#     first = int(input('Enter the first number: '))
#     second = int(input('Enter the second number: '))
#     print(first/second)
# except (ValueError, ZeroDivisionError) as ex:
#     print("ex = ", ex)
    # raise IncorrectValueNumber(ex)
# except BaseException as ex:
#     print(ex)

# class IncorrectValueNumber # пропустил что тут было :-(
#
# first = int(input('Enter the first number: '))
# second = int(input('Enter the second number: '))
# if first < 10:
#     raise IncorrectValueNumber('The number should be > 10.')
# print (first/second)
#
#
# try:
#     print(first / second)
# except ZeroDivisionError:
#     raise BaseException('You can not divide by zero.')
#     # print('You can not divide by zero.')


sample_dictionary = {'name': 'Otus', 'site': "otus.ru"}
# try:
#     print(sample_dictionary['sit'])
# except KeyError as ex:
#     raise KeyError(f'\'{ex.args[0]}\' key does not exist in dictionary')

# Второй спопоб можно
if 'site' in sample_dictionary.keys():
    print(sample_dictionary['site'])
else:
    print(f'\'site\' key does not exist in dictionary')


# если я хочу "словить" исключение (залогировать) и пойти дальше выполнять код. Как не прерывать выполнение кода после исключения?
#

# а если я заранее не знаю исключение? как обработать ВСЕ исключения (любые)?
# except BaseException as ex
# не указывать в except raise
