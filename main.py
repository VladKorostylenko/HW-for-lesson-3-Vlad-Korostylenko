# 1. Посмотреть видео и создать проект на github https://www.youtube.com/watch?v=IH0W5bm4orc

# Done

# 2. Напишите программу Python, которая принимает слово от пользователя и переворачивает его
# Пример: input - Hello Worlds output - sdlroW olleH
#
# Вариант 1
# text_input = input("Введите текст который нужно развернуть: ")
#
# res = ""
#
# for i in range(len(text_input) - 1, -1, -1):
#    res += text_input[i]
#
# print(res)

#Вариант 2
# text_input = input("Введите текст который нужно развернуть: ") [::-1]
#
# print (text_input)

# 3. Напишите программу Python для построения следующего шаблона, используя вложенный цикл for.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# height = 9
# width = 5
#
# x = 1
#
# for _ in range (0, 4):
#    print("*"*x)
#    x += 1
# for _ in range (5, 10):
#    print("*"*x)
#    x -= 1

# 4. Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B,
# или в порядке убывания если A > B

# a_count = int(input("Введите целое число А: "))
# b_count = int(input("Введите целое число B: "))
#
# list = []
#
# if a_count < b_count:
#    list.append(a_count)
#    for _ in range(a_count, b_count):
#       a_count += 1
#       list.append(a_count)
#    print(f"Диапазон между числами введёнными числами: {list}" )
# elif a_count > b_count:
#    list.append(a_count)
#    for _ in range(b_count, a_count):
#       a_count -= 1
#       list.append(a_count)
#    print(f"Диапазон между числами введёнными числами: {list}" )
#
# else:
#    print("Числа одинковые и не имеют диапазона.")

# 5. Даны два целых числа A и B (при этом A < B). Выведите все числа от A до B включительно.

# a_count = int(input("Введите целое число \"А\": "))
# b_count = int(input("Введите целое число \"B\": "))
# list = []
#
# while a_count >= b_count:
#    print("\"А\" не должно быть меньше ли равно \"B\". Попробуйте еще раз.")
#    a_count = int(input("Введите целое число \"А\": "))
#    b_count = int(input("Введите целое число \"B\": "))
#
# list.append(a_count)
# for _ in range(a_count, b_count):
#    a_count += 1
#    list.append(a_count)
# print(f"Диапазон между числами введёнными числами: {list}" )

# 6. Напишите программу, которая удаляет дубликаты элементов из списка.
#
# import random
# import itertools
#
# LIST_SIZE = int(input("Введите кол-во символов в списке: "))
# RANDOM_UPPER_BOUND = int(input("Введите макисмальный размер числа: "))
#
# l = []
# l2 = []
#
# for _ in range(0, LIST_SIZE):
#    l.append(random.randint(0, RANDOM_UPPER_BOUND))
#
# l.sort()
#
# from itertools import groupby
#
# l2 = [el for el, _ in groupby(l)]
#
# print(f"Список с дубликатами: {l}")
#
# print(f"Список без дубликатов: {l2}")

# 7. Напишите программу, которая копирует список

# import copy
# import random
# #
# LIST_SIZE = int(input("Введите кол-во символов в списке: "))
# RANDOM_UPPER_BOUND = int(input("Введите макисмальный размер числа: "))
#
# l1 = []
# l2 = []
#
# for _ in range(0, LIST_SIZE):
#     l1.append(random.randint(0, RANDOM_UPPER_BOUND))
#
# #Вариант 1
# # for i in l1:
# #     l2.append(i)
# #
# # print(l1)
# # print(l2)
#
# #Вариант 2
# l2 = copy.deepcopy(l1)
#
# print(l1)
# print(l2)




# 8. Напишите программу, которая находит разницу между двумя списками и сохраняет ее в новый список.
# Вывести результат на экран.



# 9. Напишите программу для объединения следующих словарей для создания нового



# 10. Исходные словари :
#
# dic1={1:10, 2:20}
#
# dic2={3:30, 4:40}
#
# dic3={5:50,6:60}
#
# Результат : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#



# 10. Напишите программу, которая выводит словарь, в котором ключи представляют собой числа от 1 до 15 (оба включены),
# а значения представляют собой квадраты ключей. Генерация ключей и значений должна быть выполнена через цикл.