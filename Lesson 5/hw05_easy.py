import os
import sys
import shutil

'''
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

for i in range (1, 10):  # создает
    try:  # пытается
        os.mkdir('dir_{}'.format(i))
    except FileExistsError:
        print('Такая директория уже существует')

for i in range (1, 10):  # и удаляет
    os.rmdir('dir_{}'.format(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print(os.listdir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

my_scr = sys.argv[0]
shutil.copy(my_scr, 'new.py')
'''
# эта часть отведена под функции для задания normal


def move(name):
    try:
        os.chdir(os.path.join(name))
        print('Текущая директория изменена на ' + os.getcwd())
    except FileNotFoundError:
        print('Не удалось найти указанную папку')


def look():
    my_list = os.listdir(os.getcwd())
    print('В текущей директории содержится: ')
    print(my_list)


def delete(name):
    try:
        os.rmdir(os.path.join(name))
        print('Директория ' + name + ' успешно удалена')
    except FileNotFoundError:
        print('Не удалось найти указанную папку')


def create(name):
    try:
        os.mkdir(name)
        print('Директория ', name, ' успешно создана')
    except OSError:
        print('Директория ', name, ' уже существует')
