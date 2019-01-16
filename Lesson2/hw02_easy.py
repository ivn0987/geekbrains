import random

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruts = ['яблоко', 'банан', 'киви', 'арбуз']
i = 1
for frut in fruts:
    print('{}. {:>6}'.format(i, frut))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

c = random.randrange(1, 10)  # генерируем случайные списки
d = random.randrange(1, 10)
a = []
b = []
while c != 0:
    a.append(random.randrange(1, 100))
    c -= 1
while d != 0:
    b.append(random.randrange(1, 100))
    d -= 1
    
for k in b:  # а теперь уберем элементы второго из первого, если они там есть
    count = a.count(k)
    if count != 0:
        while count != 0:
            a.remove(k)
            count -= 1
print(a, b)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

rand_num = random.randrange(1, 10)  # генерируем случайный список
first_list = []
second_list = []
while rand_num != 0:
    first_list.append(random.randrange(1, 100))
    rand_num -= 1

for i in first_list:  # получаем второй спикок из первого
    num = i % 2
    if num != 0:
        second_list.append(i * 2)
    else:
        second_list.append(i / 4)
print(first_list)
print(second_list)
