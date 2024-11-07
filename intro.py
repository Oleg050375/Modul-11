import inspect


def introspection_info(obj):
    print(f'Имя класса объекта: {obj.__class__.__name__}')  # имя класса объекта
    # print(dir(obj))
    if '__dict__' in (dir(obj)):
        print(f'Список атрибутов объекта: {list(obj.__dict__.keys())}')  # список атрибутов объекта
    else:
        print('Объект не имеет атрибутов')
    print(f'Список методов объекта: {[met[0] for met in inspect.getmembers(obj, predicate=inspect.ismethod)]}')
    try:
        print(f'Модуль-источник объекта: {inspect.getmodule(obj).__name__}')  # имя модуля, из которого взят объект
    except AttributeError:
        print('Объект не принадлежит какому-либо конкретному модулю')


class test:  # тестовый класс
    cl_attr = 1

    def __init__(self, int_attr1, int_attr2):
        self.int_attr1 = int_attr1  # str
        self.int_attr2 = int_attr2  # int

    def mix(self):  # метод в тестовом классе
        print(self.int_attr1, str(self.int_attr2 + self.cl_attr))


test_obj = test('Нечто', 17)  # объект тестового класса

# TEST ----------------------------------------------------------------------------------------------------------------

test_obj.mix()  # проверка работы метода

introspection_info(test_obj)

print(' ')

introspection_info('42')
