#1
def my_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('деление на ноль')


print(my_func(int(input('Введите первое число:')), int(input('Введите второе число: '))))

#2
def anketa(name, surname, birthday, city, phone, email):
    print(f'имя - {name}, фамилия - {surname}, дата рожения - {birthday}, город - {city}, email - {email}, тел. - {phone}')


anketa(name= 'Иван', surname= 'Иванов', birthday= '11.11.1982', city= 'Москва', email=' ivanov@mail.ru', phone= 89995555555)

#3
def max_from_two (a, b, c):
    my_list = [a, b, c]
    min_num = min(my_list)
    for i in my_list:
        if min_num == i:
            my_list.remove(i)
        return sum(my_list)


print(max_from_two(2, 4, 6))

#4
#option 1
def my_func (x, y):
    if x > 0 and type(x) == int and y < 0 and type(y) == int:
        return x ** y
    else:
        print('x- должен быть положительным целым числом; у- должен быть целым отрицательным числом.\n Введите значения заново')


print(my_func(4, -2))

#option 2
def my_func (x, y):
    if x > 0 and type(x) == int and y < 0 and type(y) == int:
        i = 0
        rez = x
        while y <= i:
            rez = rez / x
            i -=1
        return rez
    else:
        print('x- должен быть положительным целым числом; у- должен быть целым отрицательным числом.\n Введите значения заново')


print(my_func(4, -2))


#5
def sum_number():
    total = 0
    while True:
        num_list = (input('Введите числа через пробел, для выхода нажмите клавишу "q": ')).split()
        for i in range(len(num_list)):
            # почему не выходит из цикла по нажатию q
            if num_list[i] == 'q':
                break
            num_list[i] = int(num_list[i])
            total += num_list[i]
        print(total)


sum_number()

#6
int_func= lambda text: text.title()

print(int_func('text'))


