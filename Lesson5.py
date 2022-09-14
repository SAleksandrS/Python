#ДЗ к Урок5

# Задание1
# def task5_1():
#     f5_1 = open (r"task5_1.txt", "w", encoding="utf-8")
#     while True:
#         task5_1var = input("введите данные, для окончания ввода пустую строку: ")
#         if len(task5_1var) == 0:
#             f5_1.close()
#             return
#         else:
#             f5_1.write (f"{task5_1var}\n")
# task5_1()

# Задание2
# import re
# linenumber5_2 = 0
# text5_2 = ""
# with open(r'task5_2.txt', 'r', encoding='utf-8') as f5_2:
#     for line5_2 in f5_2:
#         linenumber5_2 += 1
#         text5_2 += str(line5_2)
#     result = len(re.findall(r'\w+', text5_2))
#     print(f"В файле {linenumber5_2} строк(и) и {str(result)} слов(а)")

# Задание3
# with open(r'task5_3.txt', 'r', encoding='utf-8') as f5_3:
#     text5_3 = f5_3.readlines()
#     text5_3 = [line.rstrip() for line in text5_3]
#     text5_3 = " ".join(map(str, text5_3))
#     text5_3 = text5_3.split()
#     sname = text5_3[::2]
#     money = [float(text5_3[var5_3]) for var5_3 in range (1, len(text5_3), 2)]
#     dict5_3 = dict(zip(sname, money))
# #находим счастливчиков > 20k
#     print('сотрудники с ЗП больше 20 000 руб:')
#     for lucky, value in dict5_3.items():
#         if value > 20000:
#             print(lucky, value)
# #считаем среднюю
#     cycler = 0
#     fzp = 0
#     for lucky, value in dict5_3.items():
#         cycler += 1
#         fzp += value
#     print(f'средняя зарплата всех сотрудников: {fzp/cycler}')

# Задание4
# dict5_4 = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
# with open(r'task5_4.txt', 'r', encoding='utf-8') as f5_4:
#     text5_4 = f5_4.readlines()
#     text5_4 = [line.rstrip() for line in text5_4]
#     text5_4 = " ".join(map(str, text5_4))
#     text5_4= text5_4.split()
#     text5_4new = text5_4
#     for elements in range (0, len(text5_4new)):
#         newel = dict5_4.get(text5_4new[elements])
#         if newel != None:
#             text5_4new[elements] = newel
#     for elements in range (2, len(text5_4new)-1, 3):
#         text5_4new[elements] = text5_4new[elements]+"\n"
#     for elements in range (0, len(text5_4new), 3):
#         text5_4new[elements] = text5_4new[elements] + " "
#         text5_4new[elements+1] = text5_4new[elements+1] + " "
#     text5_4new = "".join(map(str, (text5_4new)))
#     print(text5_4new)
# with open(r'task5_4new.txt', 'w', encoding='utf-8') as f5_4new:
#     f5_4new.write(text5_4new)

# Задание5
# newlist5_5 = ('1 3 4 5 69 0 3 23 4 6 7 2 1 3 4')
# with open (r'task5_5.txt', 'w', encoding='utf-8') as f5_5:
#     f5_5.write(newlist5_5)
# with open (r'task5_5.txt', 'r', encoding='utf-8') as f5_5new:
#     n=0
#     text5_5 = f5_5new.readline()
#     text5_5new = text5_5.split()
#     for elements55 in range (0, len(text5_5new)):
#         n += int(text5_5new[elements55])
#     print(f'сумма чисел равна: {n}')

# Задание(дополнительно)6
predmet = {}
hours = 0
with open(r'task5_6.txt', 'r', encoding='utf-8') as f5_6:
    text5_6 = f5_6.readlines()
    text5_6 = [line.rstrip() for line in text5_6]
    text5_6 = " ".join(map(str, text5_6))
    text5_6 = text5_6.replace('(л)', ' ')
    text5_6 = text5_6.replace('(лаб)', ' ')
    text5_6 = text5_6.replace('(пр)', ' ')
    text5_6 = text5_6.replace(':', '')
    text5_6 = text5_6.replace('—',' ')
    text5_6 = text5_6.split()
    for elements56 in (text5_6):
        try:
            hours += int(elements56)
            predmet[mempredmet] = hours
        except:
            predmet[elements56] = hours
            mempredmet = elements56
            hours = 0
    print(predmet)