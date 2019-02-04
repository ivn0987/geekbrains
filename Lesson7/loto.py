#!/usr/bin/python3
import random

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


def rand_gen15():  # сгенерируем случайные карточки
    rand_list = []
    while len(rand_list) <= 15:
        a = random.randrange(0, 99)
        if a not in rand_list:
            rand_list.append(a)
            rand_list.sort()
    card = [[str(rand_list[0]), ' ', str(rand_list[3]), str(rand_list[6]), ' ', ' ', str(rand_list[9]), str(rand_list[12]), ' '],
            [' ', ' ', str(rand_list[1]), str(rand_list[4]), str(rand_list[7]), ' ', ' ', str(rand_list[10]), str(rand_list[13])],
            [' ', str(rand_list[2]), str(rand_list[5]), ' ', str(rand_list[8]), ' ', str(rand_list[11]), ' ', str(rand_list[14])]]
    return card


def print_card():  # выведем карточки
    print('----------------' + 'Ваша карточка' + '---------------')
    for i in my_card:
        print()
        for j in i:
            print(j.rjust(4), end=' ')
    print()
    print('--------------------------------------------')
    print()
    print('------------' + 'Карточка компьютера' + '-------------')
    for i in comp_card:
        print()
        for j in i:
            print(j.rjust(4), end=' ')
    print()
    print('--------------------------------------------')


def barrels():  # тянем бочонок
    global barrels_num, list_barrels
    while barrels_num > 0:
        barrels_num -= 1
        b = random.choice(list_barrels)
        list_barrels.remove(b)
        yield b


def check_barrels():  # проверяем наличие бочонка
    for i in comp_card:
        for j in i:
            if j == bar:
                i.insert(i.index(j), '-')
                i.remove(j)
                global comp_card_not_X
                comp_card_not_X -= 1
    for i in my_card:
        for j in i:
            if j == bar:
                i.insert(i.index(j), '-')
                i.remove(j)
                global my_card_not_X
                my_card_not_X -= 1
                return True
    return False


barrels_num = 99
list_barrels = [i for i in range(0, 100)]
my_card = rand_gen15()
my_card_not_X = 15
comp_card = rand_gen15()
comp_card_not_X = 15

print('Начинаем игру!')
while barrels_num > 0:
    bar = str(next(barrels()))
    print('Новый бочонок: ' + bar + ' (осталось ' + str(barrels_num) + ')')
    print_card()
    inp = input('Зачеркнуть номер? y/n: ')
    print()
    check = check_barrels()
    if my_card_not_X == 0:
        print('Вы победили!')
        break
    elif comp_card_not_X == 0:
        print('Вы проиграли')
        break
    else:
        if inp == 'y' and check:
            continue
        elif inp == 'n' and check:
            print('Вы проиграли! Такое число есть!')
            break
        elif inp == 'y' and check == False:
            print('Вы проиграли! Такого числа нет!')
            break
        elif inp == 'n' and check == False:
            continue
