#ДЗ к Урок4

# Задание1
# from sys import argv
# print (argv)
# path, ar1, ar2, ar3 = argv
# print(f"(выработка в часах: {int(ar1)} * ставка {int(ar2)} в час) + премия {int(ar3)}) = {(int(ar1)*int(ar2))+int(ar3)} руб.")

# Задание2
# from random import *
# task4_2res = 0
# result = []
# task4_2new = [randint(0,100) for i in range (10)]
# print(task4_2new)
# for n in range (1,len(task4_2new)):
#     task4_2res = task4_2new[n]
#     if task4_2res > task4_2new[n-1]:
#        result.append(task4_2res)
# print(result)

# Задание3
#print([i for i in range (20,241) if i % 20 == 0 or i % 21 == 0])

# Задание4
# from random import *
# task4_3res = 0
# result = []
# task4_3new = [randint(0,100) for i in range (20)]
# print(task4_3new)
# for n in range (1,len(task4_3new)):
#     task4_3res = task4_3new[n]
#     retry = task4_3new.count(task4_3res)
#     if retry == 1:
#         result.append(task4_3res)
# print(result)

# Задание5
# from functools import reduce
# task4_5new = ([i for i in range (100,1001) if i % 2 == 0])
# def multiplycator(a, b):
#     return a * b
# task4_5res = reduce(multiplycator, (task4_5new))
# print(task4_5res)

# Задание6
# from itertools import count, cycle
# list4_6 = ["hello world"]
# i = 0
# for task4_6var1 in cycle(list4_6):
#     for task4_6var2 in count(3):
#         if task4_6var2 > 10:
#             break
#         print(task4_6var2)
#     i += 1
#     if i > 3:
#         break
#     print(task4_6var1)

# Задание7
from functools import reduce

task4_5var = (reduce(lambda x, y: x*y, [x for x in range(1, int(input("введите число: "))+1)]))
print(f"факториал числа равен: {task4_5var}")