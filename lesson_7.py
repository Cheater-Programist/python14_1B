# Dictionary - словари.
# str, int, bool, float, lst, tuple, set, frozenset + dict.

# student = {
#     'name' : 'Alihan',
#     'age' : 18,
# }
# print(student['name'], student['age'])
# student.setdefault('language', 'Python')
# print(student)
# print(len(student))
# print(student.get('age'))  #To get a value
# student.pop('age')  #To remowe a key with value
# print(student)
# del student['language']
# print(student)
# student['name'] = 'Nurik'  #To update a value
# print(student)
# student['address'] = "Amatova 1B" #To add a key and a value
# print(student)

# car_tesla = {
#     'id' : 103,
#     'brand' : 'Tesla',
#     'Model' : 'Model X',
#     'year' : 2023,
#     'color' : 'Black'
# }
# print(car_tesla)
# print(car_tesla['year'])
# print(car_tesla.get('id'))
# car_tesla['color'] = 'White'
# print(car_tesla)
# car_tesla.pop('year')
# print(car_tesla)
# car_tesla.setdefault('adometr', 0)
# print(car_tesla)

# import time

# lang = {
#     'Name' : 'Python',
#     'Version' : '3.11.1',
#     "date" : time.ctime(),
# }
# print(lang)

# for key, value in lang.items():
#     print(key, value)


# contact = [
#     {
#         "name" : "Nurbolot",
#         'surname' : 'Erkinbaev',
#         'phone' : '0552878777',

#     },
# ]
# print(contact)

# while True:
#     command = input("1 - view a contact, 2 - add, 3 - delete, 4 - update: ")
#     if command == "1":
#         for c in contact:
#             print(c)
#     elif command == "2":
#         add_name = input("Name: ")
#         add_surname = input("Surname: ")
#         add_num = input("Phone: ")
#         result = {'Name' : add_name, "Surname" : add_surname, "Phone" : add_num, "Created" : time.ctime()}  # {"Name :" input("Name: ")} Try it.
#         contact.append(result)
#         print("The contact added successfully")
#     elif command == "3":
#         del_num = input("Delete contact number: ")
#         for cont in contact:
#             for key, value in cont.items():
#                 if value == del_num:
#                     contact.remove(cont)
#                     print('The Contact Deleted')
#                 else:
#                     print("Undefind")


# ===============================================================================
# Functions

# def func():
#     print("Hello World!")
# func()

# def add():
#     a = int(input('Num1: '))
#     b = int(input('Num2: '))
#     print(a + b)
# add()

# def mult(a, b):
#     print(a * b)
# mult(2, 2)

# def welcome(name:str = "None") -> str:
#     print(f"Hello {name}")
# welcome("Nurik")
