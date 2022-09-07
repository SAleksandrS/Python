#ДЗ к Урок3

# Задание1
# def task3_1func(a,b):
#     if b == 0:
#         restask3_1 = "недопустимый делитель"
#     else:
#         restask3_1 = a/b
#     return restask3_1
# print(task3_1func(int(input("введите делимое: ")),int(input("введите делитель: "))))

# Задание2
# def task3_2func (name, sname, byear, town, email, phone):
#     print(f"имя: {name}, фамилия: {sname}, год рождения: {byear}, город проживания: {town}, email: {email}, телефон: {phone}")
# task3_2func(name=input("введите имя: "), sname=input("введите фамилию: "), byear=input("год рождения: "), town=input("введите город проживания: "), email=input("введите email: "), phone=input("введите номер телефона: "))

# Задание3
# def my_func(a,b,c):
#     if a > b:
#         if c > b:
#             restask3_3 = c * a
#         else: restask3_3 = a * b
#     elif a > c:
#         if b > c:
#             restask3_3 = a * b
#         else: restask3_3 = a * c
#     else: restask3_3 = b * c
#     return restask3_3
# print(my_func(int(input("введите 1 множитель: ")), int(input("введите 2 множитель: ")), int(input("введите 3 множитель: "))))

# Задание4
#   вариант1
# def task3_41func (x,y):
#     restask3_41 = x**y
#     return restask3_41
# x = int(input("введите целое положительно число: "))
# y = int(input("введите целое отрицательное число: "))
# print(f"результат: {task3_41func(x,y)}")

#   вариант2
# def task3_42func (x,y):
#      if y == 0:
#          restask3_42 = 1
#          return restask3_42
#      restask3_42 = x
#      for n in range (1,y):
#         restask3_42 = restask3_42 * (x)
#      restask3_42 = 1/restask3_42
#      return restask3_42
#
# x = int(input("введите целое положительно число: "))
# y = int(input("введите целое отрицательное число: "))*-1
# print(f"результат: {task3_42func(x,y)}")

# Задание5
# def task3_5():
#     n = 0
#     while True:
#         task3_5var = input("введите числа через пробел или stop: ").split()
#         for digits in range (0,len(task3_5var)):
#             if task3_5var[digits] == "stop":
#                 return
#             else:
#                 try:
#                     n = n + int (task3_5var[digits])
#                 except ValueError:
#                     print("обнаружена ошибка ввода данных")
#         print(f"результат: {n}")
#
# task3_5()

# Задание6 и 7

def int_func(task3_6var):
    task3_6var = task3_6var.title()
    return task3_6var
task3_6var = str(input("введите строку: ").lower())
print(int_func(task3_6var))