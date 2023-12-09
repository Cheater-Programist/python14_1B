# Модули

# 1 import model self
# import models_8

# models_8.revers_word("Bayastan")
# models_8.len_word("Hello")
# print(models_8.it)

# 2 import what we need to
# from models_8 import revers_word, len_word

# revers_word("Kurmanbek")
# len_word("asdfghjkl")

# 3 import everything
# from models_8 import *

# revers_word("Leps spel")
# len_word('leps spel')
# ==================================================

# from time import ctime
# print(ctime())


#Работва с файлами. функция open()

# f = open('test_8.txt', 'w')
# f.write('Hello world and Geeks It courses')
# f.close()

# py = open('open_8.py', 'w')
# py.write("print('Hello world')")
# py.close()

# read_py = open('lesson_7.py', 'r', encoding='utf-8') #encoding='utf-8' - to read russian words.
# print(read_py.read())
# read_py.close()


# rus = open('rus_8.txt', 'w', encoding='utf-8')
# rus.write("Всем привет как вы?")
# rus.close()

# with open('close_8.txt', 'w', encoding='utf-8') as close:  #close - переменная
#     close.write("How are you? как вы?")

# with open('close_8.txt', 'r', encoding='utf-8') as read_file:
#     print(read_file.read())