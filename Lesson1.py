# ДЗ к Урок1

# Задание1
# var1 = input("переменная 1 текстовая: ")
# var2 = int(input("переменная 2 целочисленная: "))
# var3 = float(input("переменная 3 десятичная: "))
# print(var1,"\n",var2,"\n",var3)

# Задание2
# seconds = int(input("введите целые секунды:"))
# hours = seconds//3600
# minutes = (seconds-hours*3600)//60
# seconds = (seconds-hours*3600-minutes*60)
# print(f"{hours}:{minutes}:{seconds}")

# Задание3
# magicn = (input("введите число n:"))
# magicnn = magicn+magicn
# magicnnn = magicnn+magicn
# magic = int(magicn)+int(magicnn)+int(magicnnn)
# print(f"{magicn}+{magicnn}+{magicnnn}={magic}")

# Задание4
# last = 0
# maxlast = 0
# maxvar = int(input("введите целое положительное число:"))
# while maxvar > 0:
#     last = maxvar % 10
#     if last > maxlast:
#         maxlast = last
#     maxvar //= 10
# print("максимальная цифра в числе : ", maxlast)

# Задание5
# sales = int(input("введите выличину выручки:"))
# costs = int(input("введите выличину издержек:"))
# if sales > costs: print("Прибыль")
# elif costs > sales: print("Убыток")
# else: print("Сработали в ноль")

# Задание6
# sales = int(input("введите выличину выручки:"))
# costs = int(input("введите выличину издержек:"))
# if sales > costs:
#     print("Прибыль")
#     print(f"Рентабельность: {(sales-costs)/sales*100} %")
#     labors = int(input("Введите количество сотрудников:"))
#     print(f"Прибыль на одного суотрудника: {(sales - costs) / labors}")
# elif costs > sales: print("Убыток")
# else: print("Сработали в ноль")

# Задание7
a = 0
b = 0
day = 1
a = float(input("Введите результат спортсмена в первый день: "))
b = float(input("Введите требуемый результат спортсмена: "))
while b > a:
    a *= 1.1
    day += 1
print(f"на {day} день спортсмен достигнет результата - не менее {b} км.")