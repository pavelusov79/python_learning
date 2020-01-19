#1
my_list = [1, 'string', True, [1,2,3], (4,5,6)]
for el in my_list:
    print(type(el))

#2
n = int(input('Введите число элементов списка: '))
i = 1
my_list = []
while i <= n:
    number = input(f'Введите {i}-й элемент списка: ')
    my_list.append(number)
    i += 1
j = 0
if len(my_list) % 2 == 0:
    for el in range(int(len(my_list) / 2)):
        my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        j +=2
elif len(my_list) % 2 != 0:
    for el in range(int((len(my_list) - 1) / 2)):
        my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        j +=2
print(my_list)

#3
#Option 1
month = int(input('Введите число месяца от 1 до 12: '))
my_dict = {
    1 : 'январь',
    2 : 'Февраль',
    3 : 'март',
    4 : 'апрель',
    5 : 'май',
    6 : 'июнь',
    7 : 'июль',
    8 : 'август',
    9 : 'сентябрь',
    10 : 'октябрь',
    11 : 'ноябрь',
    12 : 'декабрь'}
for key in my_dict.keys():
    if month == 12 or month == 1 or month == 2:
        print(f'Введенное числовое значение месяца "{month}" соответствует зимнему месяцу года')
        break
    elif month == 3 or month == 4 or month == 5:
        print(f'Введенное числовое значение месяца "{month}" соответствует весеннему месяцу года')
        break
    elif month == 6 or month == 7 or month == 8:
        print(f'Введенное числовое значение месяца "{month}" соответствует летнему месяцу года')
        break
    else:
        print(f'Введенное числовое значение месяца "{month}" соответствует осеннему месяцу года')
        break

#Option 2
month = int(input('Введите число месяца от 1 до 12: '))
year_months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
for key in enumerate(year_months, 1):
    if 3 <= month <= 5:
        print(f'Введенное числовое значение месяца "{month}" соответствует весеннему месяцу года')
        break
    elif 6 <= month <= 8:
        print(f'Введенное числовое значение месяца "{month}" соответствует летнему месяцу года')
        break
    elif 9 <= month <= 11:
        print(f'Введенное числовое значение месяца "{month}" соответствует осеннему месяцу года')
        break
    else:
        print(f'Введенное числовое значение месяца "{month}" соответствует зимнему месяцу года')
        break

#4
my_string = input('Введите строку разделяя слова пробелами: ')
my_string = my_string.split()
for key, item in enumerate(my_string, 1):
    if len(item) > 10:
        print(f'{key} - {item[ : 10]}')
    else:
        print(f'{key} - {item}')

#5
number = int(input('Введите число от 0 до 9: '))
my_list = [7, 5, 3, 3, 2]
for el,value in enumerate(my_list):
    if number == value:
        my_list.insert(el+1, number)
        break
    elif number > value:
        my_list.insert(el, number)
        break
else:
    my_list.append(number)
print(my_list)

#6
pos = int(input('Введите количество позиций товара: '))
i = 1
goods_list = []
while i <= pos:
    goods_name = input('введите название товара: ')
    cost = int(input('введите цену: '))
    quantity = int(input('Введите количество: '))
    item = input('введите еденицы измерения товара: ')
    my_dict = {'название' : goods_name, 'цена' : cost, 'количество' : quantity, 'ед. изм.' : item}
    goods = (i, my_dict)
    goods_list.append(goods)
    i += 1
print(goods_list)


