__author__ = 'Крымов Иван'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

numbers = [2, -5, 8, 9, -25, 25, 4]
new_numbers = []
errors = []

for num in numbers:
    if num > 0 and math.sqrt(num) % 1 == 0:
        new_numbers.append(int(math.sqrt(num)))
    else:
        errors.append(num)
print('Целые квадратные корни из списка', numbers, 'это: ', new_numbers)
print('Невозможно извлечь целые квадратные корни из: ', errors)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print()

date = '02.11.2013'
print('Дата к форматированию: ', date)
months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря',
}

days = {
    '01': 'Первое',
    '02': 'Второе',
    '03': 'Третье',
    '04': 'Четвёртое',
    '05': 'Пятое',
    '06': 'Шестое',
    '07': 'Седьмое',
    '08': 'Восьмое',
    '09': 'Девятое',
    '10': 'Десятое',
    '11': 'Одиннадцатое',
    '12': 'Двенадцатое',
    '13': 'Тринадцатое',
    '14': 'Четырнадцатое',
    '15': 'Пятнадцатое',
    '16': 'Шестнадцатое',
    '17': 'Семнадцатое',
    '18': 'Восемнадцатое',
    '19': 'Девятнадцатое',
    '20': 'Двадцатое',
    '21': 'Двадцать первое',
    '22': 'Дадцать второе',
    '23': 'Двадцать третье',
    '24': 'Двадцать четвёртое',
    '25': 'Двадцать пятое',
    '26': 'Двадцать шестое',
    '27': 'Двадцать седьмое',
    '28': 'Двадцать восьмое',
    '29': 'Двадцать девятое',
    '30': 'Тридцатое',
    '31': 'Тридцать первое',
}

new_date = date.split('.')

for key in days:
    if new_date[0] == key:
        new_date[0] = days[key]

for key in months:
    if new_date[1] == key:
        new_date[1] = months[key]

answer = new_date[0] + ' ' + new_date[1] + ' ' + new_date[2] + ' ' "года."
print('После форматирования: ', answer)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print()
from random import randint

n = randint(5, 15)
random_list = [randint(-100, 100) for i in range(n)]

print('Список заполнен ', n, ' случайными числами в диапазоне -100:100 ', random_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]

print()
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = list(set(lst))
print('Неповторяющиеся элементы списка ', lst, 'это', lst2)

# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print()
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = []
for i, el in enumerate(lst):
    c = 0
    for j, el in enumerate(lst):
        if lst[i] == lst[j]:
            c += 1
        else:
            j += 1
    if c == 1:
        lst2.append(lst[i])
print('Элементы списка', lst, ', которые не имеют повторений - это', lst2)
