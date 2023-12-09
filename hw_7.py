# Задача 1
# dict_1 = {
#     'a' : 300,
#     'b' : 400
# }
# dict_2 = {
#     'c' : 500,
#     'd' : 600
# }
# dict_1.update(dict_2)
# print(dict_1)

# Задача 2
# numbers = {
#     'num_1' : 1,
#     'num_2' : 2,
#     'num_3' :3,
#     'num_100' : 100
# }
# for k, v in numbers.items():
#     print(v * 5)

# Задача 3,4,5,6
# student = {
#     'name' : 'Askhat',
#     'age' : 17,
#     'color' : 'White'
# }
# 3)
# student['age'] *= 2
# print(student)

# 4)
# student['age'] = 16
# print(student)

# 5)
# student.pop('age')
# print(student)

# 6)
# student.setdefault('address', 'Западный Анар')
# print(student)


# Задача 7
# while True:
#     def chat_bot(a):
#         if a == "ВОТ ТАК!":
#             print("Успокойся")
#         elif "?" in a:
#             print("Конечно!")
#         elif a == '':
#             print('Как классно, когда ты молчишь. Продолжай в том же духе!')
#         else:
#             print("ну и что")
    
#     chat_bot(input("smth: "))

# Задача 8
# def frase(a : str):
#     lst = a.split(' ')
#     a = ''
#     for i in lst:
#         a += i[0]
#     print(a.upper())
# frase(input("smth: "))

# Задача 9
# a)
# def frase_words_count(a : str):
#     a = a.lower().split(",")
#     lst = "".join(a).split()
#     tup = []
#     for i in lst:
#         tup.append(i + " - " + str(lst.count(i)))
#     tup1 = set(tup)
#     print(tup1)
# frase_words_count(input("smth: "))

# b)
# def count_word(txt : str = "Hello hello") -> dict:
#     low_txt = txt.lower().split(",")
#     spacing = "".join(low_txt).split()
#     result = {}
#     for space in spacing:
#         result.setdefault(space, spacing.count(space))
#     print(result)
# count_word(input("smth: "))

# Задача 10
# def is_izogramma(word : str = "Geeks") -> bool:
#     if len(set(word)) == len(word):
#         print(True)
#     else:
#         print(False)

# is_izogramma(input("smth: "))

# Задача 11
# def num(n):
#     a = str(n)
#     a = a[::-1]
#     b = int(a)
#     print(n + b)
    
# num(int(input("smth: ")))