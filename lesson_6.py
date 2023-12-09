# Исключение - Try, Expect

# try:
#     print(100 / 0)
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")

# while True:
#     num1 = int(input("Number one: "))
#     operator = input("What's mark: ")
#     num2 = int(input("Number two: "))
#     if operator == "+":
#         print(num1 + num2)
#     elif operator == "-":
#         print(num1 - num2)
#     elif operator == "*":
#         print(num1 * num2)
#     elif operator == "/":
#         try:
#             print(num1 / num2)
#         except ZeroDivisionError:
#             print("На ноль делить нельзя!")
#     elif operator == "0" and num1 == 0 == num2:
#         print('STOP')
#         break
#     else:
#         print("Choose one of these(+,-,*,/) marks!")

# name = "N"
# try:
#     print(neme)
# except BaseException:
#     print("Whaaaaaat?!!!!")

# try:
#     print(100/0)
# except BaseException as error: #Переменная - error
#     print("Error:", error)

# raise StopIteration("Error StopIteration")

# car = "BMW"
# try:
#     print(car[3])
# except IndexError:
#     raise IndexError("Index has not definded")
# finally:
#     print("I always work")

# str, float, int, bool, lst, tuple + set, frozenset

# lst1 = [10, 20, 30, 40, 50]
# lst2 = [30, 40, 50, 60 ,70]
# print(lst1 + lst2)
# print(set(lst1 + lst2))

# names = {"Nurbolot", "Erbol", "Islam", "Erbol"}
# print(names)

# names.add("Geeks")
# print(names)
# names.add("Erbol")
# print(names)
# names.remove("Islam")
# print(names)
# names.pop()
# print(names)
# names.clear()
# print(names)

# car1 = {"BMW", "TOYOTA"}
# car2 = {"Geeks", "TOYOTA"}
# print(car1.difference(car2))

# FrozenSet
# frzn_set = frozenset({10, 10, 20, 20, 30})

# ====================================================

# import random

# random_num = random.randint(1, 10)
# # print(random_num)
# attempts = 3
# while True:
#     attempts -= 1
#     user_num = int(input("number 1-10: "))
#     if random_num == user_num:
#         print("Victory")
#         break
#     elif attempts == 0:
#         print(f"You lose, the number was {random_num}")
#         break    
#     else:
#         print(f"Is not correct, you have also {attempts}")
#         continue