__author__ = 'Крымов Иван'

import os
import shutil
import sys

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print('*' * 40)
print('Ваща текущая директория {}'.format(os.getcwd()))
print(f'Содержимое текущей папки: {os.listdir()}')
try:
    for num in range(9):
        print(f'Создана новая директория: dir_{num + 1}')
        os.mkdir('dir_{}'.format(num + 1))
except FileExistsError:
    print(f'Невозможно создать папку dir_{num + 1}, так как он уже существует')
print(f'Содержимое текущей папки: {os.listdir()}')
try:
    for num in range(9):
        print(f'Удалена директория: dir_{num + 1}')
        os.rmdir('dir_{}'.format(num + 1))
except FileNotFoundError:
    print(f'Невозможно удалить папку dir_{num + 1}, так как она не существует')
print('*' * 40)
print(f'Содержимое текущей папки: {os.listdir()}')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Данная задача реализована в задаче №1 и 3

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


print('*' * 40)
print(f'Текущая папка: {sys.argv}, исходный файл для копирования: {os.path.basename(sys.argv[0])}')
name = os.path.basename(sys.argv[0])
copy = 'copy_' + name
shutil.copy(name, copy)
print(f'Содержимое текущей папки: {os.listdir()}')
