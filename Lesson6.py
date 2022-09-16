#ДЗ к Урок6

# Задание1
# import time
# class TrafficLight:
#     color = ['red','yellow','green']
#     trafl = {'red':7, 'yellow':2, 'green':5}
#     def running(self):
#         for el in TrafficLight.trafl:
#             print(el)
#             time.sleep(TrafficLight.trafl[el])
# tr1 = TrafficLight()
# tr1.running()

# Задание2
# class Road:
#     _length = 0
#     _width = 0
#     def Calc(self, _width, _length):
#         self._width = _width
#         self._length = _length
#         return f'требуется: {(self._width*self._length*25*5)/1000} т. асфальта'
# r1 = Road ()
# print(r1.Calc(20, 10000))

# Задание3
# class Worker:
#     name = 'empty'
#     surname = 'empty'
#     position = 'empty'
#     _income = {'wage': 0, 'bonus': 0}
#
# class Position(Worker):
#
#     def get_full_name(self, name, surname):
#         self.name = name
#         self.surname = surname
#         return f'Полное имя: {self.name} {self.surname}'
#     def get_total_income(self, wage, bonus):
#         Worker._income['wage'] = wage
#         Worker._income['bonus'] = bonus
#         return Worker._income['wage']+Worker._income['bonus']
#
# work1 = Position()
# print(work1.get_full_name('Иван','Иванов'))
# print(f'Итого доход: {work1.get_total_income(10000, 5000)}')

# Задание4
# class Car:
#     speed = 0
#     color = 'nocolor'
#     name = 'unknown'
#     is_police = False
#
#     def __init__(self, speed, color, name, is_police):
#         Car.speed = speed
#         Car.color = color
#         Car.name = name
#         Car.is_police = is_police
#     def show_speed(self):
#         if Car.speed == 0:
#             return f'{Car.color} {Car.name} Stand still because speed is {Car.speed} km/h'
#         elif Car.speed > 60:
#             return f'{Car.color} {Car.name} Speed {Car.speed} km/h is to high!!!'
#         else:
#             return f'{Car.color} {Car.name} In motion {Car.speed} km/h'
#
#     def go(self, speed):
#         Car.speed = speed
#         return f'{Car.color} {Car.name} Starting and speed is {Car.speed} km/h'
#
#     def stop(self):
#         Car.speed = 0
#         return f'{Car.color} {Car.name} Stoping, stand still because speed is {Car.speed} km/h'
#
#     def turn(self,Directions):
#         self.Directions = Directions
#         return f'It turns {Directions}'
#
# class TownCar(Car):
#     def __init__(self,speed, color, name, is_police):
#         Car.__init__(self, speed, color, name, is_police)
#
# class SportCar(Car):
#     def __init__(self,speed, color, name, is_police):
#         Car.__init__(self, speed, color, name, is_police)
#
# class WorkCar(Car):
#     def __init__(self,speed, color, name, is_police):
#         Car.__init__(self, speed, color, name, is_police)
#
# class PoliceCar(Car):
#     def __init__(self,speed, color, name, is_police):
#         Car.__init__(self, speed, color, name, is_police)
#
# car1 = TownCar(70, 'White', 'Toyota', False)
# print(car1.show_speed())
# print(car1.turn('left'))
# print(car1.stop())
# print(car1.show_speed())
# print(car1.go(40))
# print(car1.show_speed())
#
# car2 = PoliceCar(80, 'Black', 'Ford', True)
# print(car1.show_speed())
# print(car1.turn('right'))
# print(car1.stop())
# print(car1.go(80))

#Задание5
class Stationery:
    title = 'Empty'
    def draw(self):
        return f'Запуск отрисовки {Stationery.title}'
class Pen(Stationery):
    def __init__(self):
        Stationery.draw(self)
        Stationery.title = 'Pen'

class Pencil(Stationery):
    def __init__(self):
        Stationery.draw(self)
        Stationery.title = 'Pencil'

class Handle(Stationery):
    def __init__(self):
        Stationery.draw(self)
        Stationery.title = 'Handle'

stat1 = Pen()
print(stat1.draw())

stat2 = Pencil()
print(stat1.draw())

stat3 = Handle()
print(stat1.draw())