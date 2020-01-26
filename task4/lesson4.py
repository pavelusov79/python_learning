from sys import argv

print('----1----')
script_name, first_param, second_param, third_param = argv
print( "Имя скрипта: " , script_name)
print( f"Выработка в часах: {first_param} ч")
print( f"Ставка в час: {second_param} руб/ч")
print( f"Премия: {third_param} руб.")
rezult = int(first_param) * int(second_param) + int(third_param)
print(f'Заработная плата составляет: {rezult} руб.')


#2
print('----2----')
my_list = [2, 21, 0, 66, 121, -5, 140]
new_list = [el+1 for el in my_list]
print(new_list)


#3
print('----3----')
my_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list)


#4
print('----4----')
my_list = [0, -5, -5, 24, 63, 12, 0, 24, 38, 2, 12, 15]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)


#5
print('----5----')
from functools import reduce
my_list =[el for el in range(100, 1001) if el % 2 == 0]
multiply_all = reduce(lambda x,y: x * y, my_list)
print(multiply_all)


#6
print('----6----')
from itertools import count, cycle
for el in count(25):
    if el > 40:
        break
    else :
        print(el)

my_list = [1, 2, 3, 4, 5]
c = 0
for el in cycle(my_list):
    if c <= 14:
        print(el)
        c +=1
    else:
        break


#7
print('----7----')
def fibo_gen():
    my_generator = (el for el in range(1, 20))
    for el in my_generator:
        yield (el)
rez = 1
for el in fibo_gen():
    if el > 15:
        break
    else:
        rez = rez * el
        print(f'факториал числа {el} равен {rez}')