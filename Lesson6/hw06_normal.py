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


class School:
    def __init__(self):
        global list_classes
        pass

    def list_class(self):
        print('Список классов в школе: ')
        list_class = list_classes.keys()
        for i in list_class:
            print(i)

class Class(School):
    def __init__(self, class_name, *teacher_name):
        School.__init__(self)
        self.class_name = class_name
        self.teacher_name = teacher_name
        list_class = list_classes.get(self.class_name)
        if list_class == None:
            list_classes[self.class_name] = {'students': [], 'teachers': []}

    def list_class(self):
        print('Список учеников ' + self.class_name + ' класса: ')
        list_class = list_classes.get(self.class_name)['students']
        for i in list_class:
            print(i)

    def list_teachers(self):
        print('В ' + self.class_name + ' классе преподают:')
        list_teachers = list_classes.get(self.class_name)['teachers']
        for i in list_teachers:
            print(i)

class People:
    def __init__(self, surname, name):
        self.name = name
        self.surname = surname


class Student(People):
    def __init__(self, surname, name, class_name, first_parent, second_parent):
        People.__init__(self, surname, name)
        self.class_name = class_name
        self.full_name = surname + ' ' + name[0] + '.'
        self.first_parent = first_parent
        self.second_parent = second_parent
        list_class = list_classes.get(self.class_name)
        if list_class == None:
            list_classes[self.class_name] = {}
        else:
            list_classes[self.class_name]['students'].append(self.full_name)

    def get_parents(self):
        print('Родители ученика: ' + self.first_parent + ' и ' + self.second_parent)

    def get_theme(self):
        teachers = list_classes.get(self.class_name)['teachers']
        print('Ученик ' + self.full_name + ' изучаев предметы:')
        for j in teachers:
            print(list_teachers.get(j))



class Teacher(People):
    def __init__(self, surname, name, theme, *teach_classes):
        People.__init__(self, name, surname)
        self.theme = theme
        self.teach_classes = teach_classes
        self.full_name = surname + ' ' + name[0] + '.'
        for i in self.teach_classes:
            list_class = list_classes.get(i)
            if list_class != None:
                list_classes[i]['teachers'].append(self.full_name)
        list_teachers[self.full_name] = self.theme


list_classes = {}
list_teachers = {}

school = School()
class_a = Class('5А', 'Математиков Математик', 'Историков Историк', 'Физиков Физик')
class_b = Class('6А', 'Математиков Математик', 'Физиков Физик')
class_c = Class('7А', 'Историков Историк', 'Физиков Физик')
person1 = Student('Иванов', 'Иван', '5А', 'Иванов Петр Васильевич', 'Иванова Мария Ивановна')
person2 = Student('Петров', 'Петр', '5А', 'Петров Иван Исакович', 'Петрова Анна Ивановна')
person3 = Student('Сидоров', 'Сидор', '6А', 'Сидоров Виктор', 'Сидорова Юлия')
person4 = Student('Абрамов', 'Исаак', '6А', 'Абрамов Моисей', 'Абрамова Сара')
person5 = Student('Алексеев', 'Алексей', '7А', 'Алексеев Александр', 'Алексеева Ольга')
person6 = Student('Александров', 'Александр', '7А', 'Александров Петр', 'Александрова Светлана')
person7 = Teacher('Математиков', 'Математик', 'математика', '5А', '6А', '7А')
person8 = Teacher('Историков', 'Историк', 'история', '5А', '7А')
person9 = Teacher('Физиков', 'Физик', 'физика', '6А', '7А')

person2.get_parents()

class_b.list_class()

school.list_class()

class_a.list_teachers()

person6.get_theme()
