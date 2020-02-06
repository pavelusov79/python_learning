#1
import random
class Matrix:
    def __init__(self, matr):
        self.matr = matr
        self.a = [random.randint(1,10) for i in range(matr)]
        self.b = [random.randint(1,10) for i in range(matr)]
        self.matrix = [self.a, self.b]

    def __add__(self, other):
        return (list(map(lambda x, y: x + y, self.a, other.a)), list(map(lambda x, y: x + y, self.b, other.b)))

    def __str__(self):
        print(f'матрица {self.matrix}')

matrix_1 = Matrix(3)
matrix_2 = Matrix(3)
matrix_1.__str__()
matrix_2.__str__()
new = matrix_1 + matrix_2
print(f'сложенная матриаца {new}')

#2
''' если честно я не понял как сделать с абстрактным классом, поэтому сделал 
в двух вариантах через один клас и с дочерним классом'''
class Clothes:
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    @property
    def get_size(self):
        return (self.size / 6.5 + 0.5)

    def get_height(self):
        return (2 * self.height + 0.3)

palto = Clothes('Пальто', 46, 180)
print(f'Размер пальто: {palto.size}')
print(f'Раcход ткани для пальто равен: {round(palto.get_size, 2)}')

suit = Clothes('Костюм', 46, 180)
print(f'Рост клиента для расчета ткани косюма: {suit.height}')
print(f'Раcход ткани для костюма равен: {round(suit.get_height(), 2)}')
print()

class Clothes:
    def __init__(self, name):
        self.name = name

class Type(Clothes):
    v = 46
    h = 180

    @property
    def size(self):
        return (self.v / 6.5 + 0.5)

    @property
    def height(self):
        return (2 * self.h + 0.3)

palto = Type('Пальто')
print(f'Размер пальто: {palto.v}')
print(f'Раcход ткани для пальто равен: {round(palto.size, 2)}')

suit = Type('Костюм')
print(f'Рост клиента для расчета ткани косюма: {suit.h}')
print(f'Раcход ткани для костюма равен: {round(suit.height, 2)}')

#3
class Kletka:
    rez = 0
    def __init__(self, q):
        self.q =q

    def __add__(self, other):
        return self.q + other.q

    def __sub__(self, other):
        if self.q > other.q:
            return self.q - other.q
        else:
            return 'отнять невозможно'

    def __mul__(self, other):
        return self.q * other.q

    def __truediv__(self, other):
        return round(self.q / other.q)

    def __str__(self):
        return f'{self.q}'

    def make_order(self, row):
        self.row = row
        pass
    '''что конкретно должно выводиться в виде **\n\n**
    вместо звездочек цифры или наборот звездочки?
    В описании не разобрался если 12 ячеек то вид **\n\n, а если
    15 то вид **\n\n***'''

q_1 = Kletka(124)
q_2 = Kletka(45)

rez_1 = q_1 + q_2
rez_2 = q_1 - q_2
rez_3 = q_1 *  q_2
rez_4 = q_1 / q_2

print(rez_1, rez_2, rez_3, rez_4, sep='\n')
