# Задача 1
# Мое мнение об исключении - предугадывать действия пользователя, то есть если я создам сайт
# и если хочу сделать некие изменения в какой то странице этого сайта, я могу написать на эту страницу
# исключение, следственно пользователю не засветится ошибка самого кода, а моё исключение, и пользователь
# не испугается от увиденного.

# Задача 2
# num = 1
# try:
#     print(number)
# except NameError:
#     raise IndexError("Index Error")

# Задача 3
# nums = input("Type some numbers(after comma): ")
# lst = nums.split(',')
# print(set(lst))

# Задача 4
# while True:
#     try:
#         num1 = int(input("Type number one: "))
#         num2 = int(input("Type number two: "))
#     except ValueError:
#         print("Type a number! Try again")
#         continue

#     if (num1 + num2) % 2 == 0:
#         try:
#             print(f"Сумма: {num1 + num2}, Разность: {num1 - num2}, умножение: {num1 * num2}, Деление: {num1 / num2}, Сумма четная.")
#         except ZeroDivisionError:
#             print("Try again")
#             continue
#     else:
#         try:
#             print(f"Сумма: {num1 + num2}, Разность: {num1 - num2}, умножение: {num1 * num2}, Деление: {num1 / num2}, Сумма нечетная.")
#         except ZeroDivisionError:
#             print("Try again")
#             continue