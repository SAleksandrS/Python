#ДЗ к Урок8

# Задание1
# class Data():
#     def __init__(self, date, month, year):
#         self.d = date
#         self.m = month
#         self.y = year
#
#     @classmethod
#     def set_date(cls, fdate):
#         fdate = fdate.split('-')
#         date, month, year = fdate
#         return cls(date, month, year)
#
#     @staticmethod
#     def get_date(obj):
#         if int(obj.d) < 1 or int(obj.d) > 31:
#             return 'ошибка в числе дня'
#         elif int(obj.m) < 1 or int(obj.m) > 12:
#             return 'ошибка в числе месяца'
#         elif int(obj.y) < 1 or int(obj.y) > 2022:
#             return 'ошибка в числе года'
#         else:
#             return f'день: {obj.d} месяц: {obj.m} год: {obj.y}'
#
# dat = '23-09-2022'
# d1 = Data.set_date(dat)
# print(Data.get_date(d1))

# Задание2
# class Divex(Exception):
#     def __init__(self,parametr):
#         self.parametr = parametr
#
# indat1 = input('введите делимое: ')
# indat2 = input('введите делитель: ')
# try:
#     indat1 = int(indat1)
#     indat2 = int(indat2)
#     if indat2 == 0:
#         raise Divex('деление на нулевое значение невозможно')
# except (ValueError, Divex) as err:
#     print(err)
# else:
#     print(f'результат деления: {indat1 / indat2}')
# finally:
#     print('завершение программы')

# Задание3
# class Inpexept(Exception):
#     def __init__(self, parametr):
#          self.parametr = parametr
#
# def task8_3():
#     n = 0
#     while True:
#         task8_3var = input("введите числа через пробел или stop: ").split()
#         for digits in range (0, len(task8_3var)):
#             if task8_3var[digits] == "stop":
#                 return
#             else:
#                 try:
#                     n = n + int (task8_3var[digits])
#
#                 except (ValueError, Inpexept) as err:
#                     del task8_3var[digits]
#                     print(err)
#
#         print(f"результат: {task8_3var}")
#
# task8_3()

# Задание4

class Warex(Exception):
    def __init__(self,parametr):
        self.parametr = parametr

class Warehouse():
    def __init__(self, quantity):
        try:
           self.quantity = int(quantity)
        except (ValueError, Warex) as error:
            print(error)

class Computerparts(Warehouse):
    def __init__(self, quantity, vendor):
        super().__init__(quantity)
        self.vendor = vendor

class Cpu(Computerparts):
    def __init__(self, quantity, vendor, socket):
        super().__init__(quantity, vendor)
        self.socket = socket

    def __str__(self):
        return f'CPU {self.quantity} ед., сокет: {self.socket}, производитель: {self.vendor}'

class Motherboard(Computerparts):
    def __init__(self, quantity, vendor, socket):
        super().__init__(quantity, vendor)
        self.socket = socket


    def __str__(self):
        return f'Motherboard {self.quantity} ед., сокет: {self.socket}, производитель: {self.vendor}'

class Memory(Computerparts):
    def __init__(self, quantity, vendor, memtype):
        super().__init__(quantity, vendor)
        self.memtype = memtype

    def __str__(self):
        return f'Memory {self.quantity} ед., производитель: {self.vendor}, тип памяти {self.memtype}'


cp1 = Cpu(3, 'AMD', 'AM4')
cp2 = Motherboard(3, 'ASUS', 'AM4')
cp3 = Memory(6, 'Crucial', 'DDR4')

print(cp1)
print(cp2)
print(cp3)
