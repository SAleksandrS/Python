# ДЗ к Урок2

# Задание1
# task1var = ["переменная","список","задания","№",1,True]
# for t1 in task1var:
#     print(type(t1))

# Задание2
# task2var = input("введите список:").split()
# for t2 in range(1, len(task2var), 2):
#      task2var[t2-1], task2var[t2] = task2var [t2], task2var [t2-1]
# print(task2var)

# Задание3
# task3var = {1:"зима", 2:"зима", 3:"весна", 4:"весна", 5:"весна", 6:"лето", 7:"лето", 8:"лето", 9:"осень", 10:"осень", 11:"осень", 12:"зима"}
# month3 = int(input("номер месяца (1-12): "))
# print(task3var.get(month3))

# Задание4
# task4var = input("введите слова:").split()
# for count4, t4 in enumerate(task4var):
#     if len(t4) > 10: t4 = t4 [0:10]
#     print(f"{count4}, {t4}")

# Задание5
# task5var = [7, 5, 3, 3, 2]
# input5var = int(input("введите число: "))
# for t5 in range(0, len(task5var)):
#     if input5var > task5var[t5]:
#         task5var.insert(t5,input5var)
#         break
#     if t5 >= (len(task5var))-1:
#         task5var.append(input5var)
#         break
# print(task5var)

# Задание6
sale6 =()
dict6 = {} #пустой словарь для {"название": " ", "цена": 0, "количество": 0, "eд": " "}
for count6 in range (3):
    dict6["название"] = input("название: ")
    dict6["цена"] = input("цена: ")
    dict6["количество"] = input("количество: ")
    dict6["ед"] = input("единицы измерения: ")
    sale6 = (count6, dict6) #здесь надо сгенерировать уникальный кортеж, но как?
    print(sale6)
    print(type(sale6))
