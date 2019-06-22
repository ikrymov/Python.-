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

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def cp(file):
    name_pattern = os.path.basename(file) + '.' + 'copy' + '.' + \
                   time.strftime("%d-%m-%Y_%H%M%S")

    with open(__file__, 'rb') as src:
        with open(name_pattern, 'wb') as dest:
            dest.write(src.read())
            dest.close()
            src.close()
    pass


def rm(file):
    try:
        os.remove(file)
        print(f"Dir {file} removed")
    except FileNotFoundError:
        print(f"Dir {file} Not exist")
    pass


def cd(dir):
    os.chdir(dir)


def ls(var):
    print(os.getcwd())
