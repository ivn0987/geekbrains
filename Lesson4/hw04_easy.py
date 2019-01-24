import random
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
first_list = [random.randint(-10, 10) for _ in range(10)]  # получаем первый рандомный список
print(first_list)
second_list = [i ** 2 for i in first_list]  # получаем второй список из квадратов элементов первого
print(second_list)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
first_fruit_list = ['яблоко', 'груша', 'абрикос', 'ананас']
second_fruit_list = ['яблоко', 'киви', 'груша', 'банан']
print([i for i in first_fruit_list if second_fruit_list.count(i) != 0]) # каждый i в первом списке, который входит во второй не 0 раз

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list1 = [random.randint(-100, 100) for _ in range(10)]
print(list1)
print([i for i in list1 if ((i % 3 == 0) and (i > 0) and (i % 4 != 0))])