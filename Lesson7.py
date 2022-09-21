#ДЗ к Урок7

# Задание1
# class Matrix:
#     def __init__(self, m):
#         self.m = m
#
#     def __str__(self):
#         for i in range (0, len(self.m)):
#             for j in range (0,len(self.m[i]), 2):
#                 print(f'--------- \n| {self.m[i][j]} | {self.m[i][j+1]} |')
#         print(f'---------')
#         return ''
#     def __add__(self, other):
#         for i in range(0, len(self.m)):
#             for j in range(0, len(self.m[i]), 2):
#                 print(f'--------- \n| {self.m[i][j] + other.m[i][j]} | {self.m[i][j + 1] + other.m[i][j + 1]} |')
#         print(f'---------')
#         return ''
#
# m = [[2,3],[3,2],[4,2]]
# n = [[1,2],[4,3],[5,3]]
# a = Matrix (m)

# b = Matrix (n)
# print(a)
# print(b)
# print(a + b)

# Задание2
# class Wearing:
#     def __init__(self, parametr):
#         self.__parametr = parametr
#     @property
#     def p(self):
#         return self.__parametr
#     @p.setter
#     def p(self,parametr):
#         self.__parametr = parametr
#
# class Coat(Wearing):
#     def __init__(self, parametr):
#         Wearing.__init__(self, parametr)
#     def __str__(self):
#         return f'для пальто требуется {(self.p/6.5 + 0.5)} метров ткани'
#
# class Suit(Wearing):
#     def __init__(self, parametr):
#         Wearing.__init__(self, parametr)
#     def __str__(self):
#         return f'для костюма требуется {self.p*2 + 0.3} метров ткани'
#
# v = Coat(52)
# h = Suit(5)
# print (v)
# print (h)

# Задание3
class Cell:
    nucleus = 0
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __str__(self):
        return f'{self.nucleus}'

    def __add__(self, other):
        return Cell(self.nucleus+other.nucleus)

    def __sub__(self, other):
        self.temp = self.nucleus-other.nucleus
        if self.temp < 0:
            return 'результат отрицательный - ошибка данных'
        else:
            return Cell(self.nucleus-other.nucleus)

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(self.nucleus // other.nucleus)

    def make_order(self, nuc_row):
        self.nuc_row = nuc_row
        self.temp = self.nucleus // self.nuc_row

        for i in range(self.temp):
            print('*'*self.nuc_row)
        print('*'*(self.nucleus-(self.temp*self.nuc_row)))
        return ''

c1 = Cell(5)
c2 = Cell(3)
c3 = Cell(1)
c4 = Cell(17)
print(c1 - c2 / c3)
print(c4.make_order(5))