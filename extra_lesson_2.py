# season = int(input("Type from 1 to 12: "))

# if 3 <= season <= 5:
#     print(f"{season} - Весна")
# elif 6 <= season <= 8:
#     print(f"{season} - Лето")
# elif 9 <= season <= 11:
#     print(f"{season} - Осень")
# elif season == 12 or 1 <= season <= 2:
#     print(f"{season} - Зима")
# else:
#     print("Type from 1 to 12")

# sum = int(input("Type the sum: "))
# if sum >= 1000:
#     a = (sum / 100) * 10
#     print(f"Your chek is {int(sum - a)}")
# else:
#     print(f"Your chek is {sum}")

# sum = int(input("Type from 100 to 1000: "))

# if 100 <= sum <= 199:
#     print("Bought Pepsi")
# elif 200 <= sum <= 299:
#     print("Bought flash")
# elif 300 <= sum <= 399:
#     print("Bought burn")
# elif 400 <= sum <= 499:
#     print("Bought gorilla")
# elif 500 <= sum <= 599:
#     print("Bought J7")
# elif 600 <= sum <= 699:
#     print("Bought legenda")
# elif 700 <= sum <= 799:
#     print("Bought Asu")
# elif 800 <= sum <= 899:
#     print("Bought Cola")
# elif 900 <= sum <= 999:
#     print("Bought fanta")
# elif 1000 == sum:
#     print("Bought all")
# elif sum < 99:
#     print("Didn't buy anything")
# else:
#     print("Type from 100 to 1000")



# count = 0

# while True:
#     num = int(input("Type a number: "))
#     if num == 0:
#         break
#     else:
#         count += num
#         print(count)

# num = int(input("Type number: "))
# count = 1

# for i in range(10):
#     print(f"{count} * {num} = {num * count}")
#     count += 1


num1 = int(input("First number: "))
num2 = int(input("Second number: "))

lstr = []

for i in range(num1, num2 + 1):
    a = i - 1
    if i % i == 0 and i % 2 == 0:
        lstr.append(i)

print(f"Простое число - {[lstr]}")