# Циклы - For, While
# For

# for i in range(1001):
#     print(i)

# for i in range(1, 101):
#     print(f'{i}) Geeks')

# for n in range(0,102,2):
#     print(f'{n}) Geeks')

# for num in range(2,201):
#     if num % 2 == 0:
#         print(f"{num} - even")
#     else:
#         print(f"{num} - odd")

# cars = ['BMW', "LEXUS", 'TOYOTA', 'BYD', "Zeekr"]
# print(cars)
# print(len(cars))

# for car in cars:  #Iteration
#     print(car)

# name = 'Nurbolot'
# 
# for n in name:
    # if n == "b":
        # print("b is here")

# num = (12, 32, 3, 4, 4, 23, 50, 87)

# for i in num:
#     if i % 2 == 0:
#         print(f"{i} - even")
#     else:
#         print(f"{i} - odd")

# import random

# password_len = int(input("What's the length of your password: "))
# password_qty = int(input("What's the quantity of your password: "))
# letters = "qwertyuiopasdfghjklzxcvbnm1234567890 "

# for q in range(password_qty):
#     result = ""
#     for i in range(password_len):
#         choice = random.choice(letters)
#         result += choice
#     print(result)

# While

# num1 = 10
# num2 = 20

# while num1 < num2:
#     num1 += 1
#     print(num1)

# n = 0
# while True:
#     n += 100
#     print(n)
#     if n == 1000:
#         print("STOP")
#         break
#     else:
#         continue

# for i in range(0,1000):
#     print(i)
#     if i == 1000:
#         print('STOP')
#         break
#     else:
#         continue

# import time

# progress = 0
# while True:
#     time.sleep(3) #Время задержки вывода
#     progress += 10
#     print(f"Hacking {progress}%")
#     if progress == 100:
#         print("Hacked")
#         break