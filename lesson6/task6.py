#1
import time
class TrafficLight():
    __color = ['red', 'yellow', 'green']
    def running(self):
        while True:
            for i in self.__color:
                print(i)
                if i == 'yellow':
                    time.sleep(2)
                else:
                    time.sleep(7)

light_1 = TrafficLight()
print(light_1.running())

#2
class Road():
    __length = int(input('Введите длину автодороги в метрах: '))
    __width = int(input('Введите ширину автодороги в м: '))
    def rachet_tonn(self):
        rezult = self.__length * self.__width * 25 * 5
        print(f'Необходимо {rezult} тонн асфальта для дороги длиной {self.__length}  и шириной {self.__width} при толщине укладки 5 см')

road_1 = Road()
road_1.rachet_tonn()

#3
class Woker():
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income
        wage = 0
        bonus = 0
        _income = {'wage': wage, 'bonus':bonus}

class Position(Woker):
    def get_full_name(self):
        print(f'Полное имя: {self.surname} {self.name}')
    def get_total_income(self):
        sum_t= 0
        for value in self._income.values():
            sum_t += value
        print(f'Общая сумма дохода: {sum_t} руб.')

worker_1 = Position('Ivan Ivanovich', 'Ivanov', 'woker', {'wage':30000, 'bonus':20000})
worker_1.get_full_name()
worker_1.get_total_income()

#4
class Car():
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина свернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Ограничение скорости 60 км/ч!')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Ограничение скорости 40 км/ч!')

class SportCar(Car):
    model = 'Impreza WRX'

class PoliceCar(Car):
    type = 'Патрульная'


bus = TownCar('автобус','желтый', 70, False)
print(f'название авто - {bus.name}\n цвет - {bus.color}\n скорость - {bus.speed}км/ч\n полиция - {bus.is_police}')
bus.go()
bus.show_speed()
bus.turn('налево')
bus.stop()

truck = WorkCar('грузовик', 'серый', 50, False)
print(f'название авто - {truck.name}\n цвет - {truck.color}\n скорость - {truck.speed}км/ч\n полиция - {truck.is_police}')
truck.go()
truck.show_speed()
truck.turn('направо')
truck.stop()

car_1 = SportCar('болид Formula 1', 'red', 200, False)
print(f'название авто - {car_1.name}\n модель - {car_1.model}\n цвет - {car_1.color}\n скорость - {car_1.speed}км/ч\n полиция - {car_1.is_police}')
car_1.go()
car_1.show_speed()
car_1.turn('направо')
car_1.stop()

car_2 = PoliceCar('Специальное авто', 'бело-синяя', 100, True)
print(f'название авто - {car_2.name}\n тип - {car_2.type}\n цвет - {car_2.color}\n скорость - {car_2.speed}км/ч\n полиция - {car_2.is_police}')
car_2.go()
car_2.show_speed()
car_2.turn('направо')
car_2.stop()

#5
class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Ручка пишет синим цветом')

class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует черным цветом')

class Handle(Stationery):
    def draw(self):
        print('Маркер желтый')

stationery_1 = Stationery('выделитель текста')
stationery_2 = Pen('шариковая ручка')
stationery_3 = Pencil('карандаш для рисования')
stationery_4 = Handle('маркер для доски')

stationery_1.draw()
stationery_2.draw()
stationery_3.draw()
stationery_4.draw()
