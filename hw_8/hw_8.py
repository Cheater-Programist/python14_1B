# Задача 1
# import random

# language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]

# def lang(lst : list = language) -> str:
#     ran_choice = random.choice(lst)
#     print(ran_choice)
#     with open('hw_8/language.txt', 'w') as close:
#         close.write(ran_choice)

# lang()

# Задача 2
# text = """
#     Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.
# """

# txt_file_1 = open('hw_8/text.txt', 'w')
# txt_file_1.write(text)
# txt_file_1.close()

# with open('hw_8/text.txt', 'w') as txt_close:
#     txt_close.write(text)

# Задача 3
# with open('hw_8/wikipedia.txt', 'w') as close:
#     f = open('hw_8/text.txt', 'r')
#     close.write(f.read())
#     f.close()