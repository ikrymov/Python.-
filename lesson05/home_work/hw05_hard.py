__author__ = 'Крымов Иван'
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
import os
import sys
import time

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - скопировать файл")
    print("rm <file_name> - удалить файл")
    print("cd <directory> - перейти в директорию")
    print("ls - отображение полного пути текущей директории")


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


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key](sys.argv[2])
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

from easy import *


def main():
    while True:
        print('''1 Перейти в папку
2 Просмотреть содержимое текущей папки
3 Удалить папку
4 Создать папку
5 ping 
6 Cкопировать файл
7 Удалить файл
8 Отображение полного пути текущей директории
q Выход''')
        task = input()

        if task == 'q':
            print('goodbye')
            break

        elif task == '1':
            dirname = input('Введите название папки для перехода: ')
            changedir(dirname)

        elif task == '2':
            currentdir()

        elif task == '3':
            dirname = input('Введите название папки, которую необходимо удалить: ')
            removedir(dirname)

        elif task == '4':
            dirname = input('Введите название новой папки: ')
            makedir(dirname)

        elif task == '5':
            ping()
        elif task == '6':
            dirname = input('Введите название файла для копирования: ')
            cp(dirname)
        elif task == '7':
            dirname = input('Введите название файла для удаления: ')
            rm(dirname)
        elif task == '8':
            ls()


main()
