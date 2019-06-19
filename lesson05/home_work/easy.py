__author__ = 'Крымов Иван'

import os

def makedir(name):
    try:
        os.mkdir(name)
        print(f'Папка {name} успешно создана')
    except FileExistsError:
        print(f'Невозможно создать папку {name}, так как он уже существует')

def removedir(name):
    try:
        os.rmdir(name)
        print(f'Папка {name} успешно удалена')
    except FileNotFoundError:
        print(f'Невозможно удалить папку {name}, так как она не существует')

def currentdir():
    print(f'Содержимое текущей папки: {os.listdir()}')

def changedir(name):
    file_list = os.listdir()
    if name in file_list:
        os.chdir(name)
        print(f'Вы успешно перешли в папку {name}', os.getcwd())
    else:
        print('Такой папки не существует!')
