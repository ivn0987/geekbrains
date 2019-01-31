# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = surname + name[0] + '.'
        self.school = school


class Student(People):
    def __init__(self, name, surname, class_room):
        People.__init__(self, name, surname)
        self._class_room = class_room


class Teacher(People):
    def __init__(self, name, surname, teach_classes):
        People.__init__(self, name, surname)
        self.teach_classes = teach_classes


class Parent(People):
    def __init__(self, name, surname):
        People.__init__(self, name, surname)


school = School()
class_a = Class('5A')
class_b = Class('6A')
class_c = Class('7A')
person1 = Student('Иванов', 'Иван', 'Иванов Петр Васильевич', 'Иванова Мария Ивановна')
person2 = Student('Петров', 'Петр', 'Петров Иван Исакович', 'Петрова Анна Ивановна')
person3 = Teacher('Учителев', 'Учитель', 'математика')

print(School.list_classes())





