import math
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = [1, 1]
    for i in range(m + 1):
        fib.append(fib[i] + fib[i + 1])
    return fib[n - 1: m - 1]

print(fibonacci(10, 20))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sort_list = []
    min = origin_list[0]
    while len(origin_list) > 1:
        for i in origin_list:
            if i < min:
                min = i
        sort_list.append(min)
        origin_list.remove(min)
        min = origin_list[0]
    sort_list.append(min)
    return sort_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(function_object, iterable):
    iter_list = []
    for i in iterable:
        if function_object(i) == True:
            iter_list.append(i)
    return iter_list

print(my_filter(lambda x: x + 2 == 3, [1, 2, 3, 5, 6, 8]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

a1x = int(input('Введите координату x точки А1: '))
a1y = int(input('Введите координату y точки А1: '))
a2x = int(input('Введите координату x точки А2: '))
a2y = int(input('Введите координату y точки А2: '))
a3x = int(input('Введите координату x точки А3: '))
a3y = int(input('Введите координату y точки А3: '))
a4x = int(input('Введите координату x точки А4: '))
a4y = int(input('Введите координату y точки А4: '))
if a1y == a4y and a2y == a3y and abs(a1x - a2x) == abs(a3x - a4x):
    print('Точки являются вершинами параллелограмма')
else:
    print('Точки не являются вершинами параллелограмма')