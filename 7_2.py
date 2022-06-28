# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property

from abc import ABC, abstractmethod


class Clothes(ABC):
    look = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def expense(self):
        pass

    def __add__(self, other):
        Clothes.look += self.expense + other.expense
        return Coat(0)

    def __str__(self):
        result = Clothes.look
        Clothes.look = 0
        return f"Общий расход ткани: {result}"


class Costume(Clothes):
    @property
    def expense(self):
        return round(2 * int(self.param) + 0.3)


class Coat(Clothes):
    @property
    def expense(self):
        return round(int(self.param) / 6.5 + 0.5)


costume_1 = Costume(162)
coat_1 = Coat(42)
coat_2 = Coat(55)
print(coat_1 + costume_1 + coat_2)

