# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
# (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом
# проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора
# @property.

from abc import ABC, abstractmethod

class Things(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

class Coat(Things):

    @property
    def consumption(self):
        return round(self.param/6.5, 2) + 0.5


class Suit(Things):

    @property
    def consumption(self):
        return 2 * self.param + 0.3

collar = Coat(15)
pockets = Coat(12)
back = Coat(70)
sleeves = Coat(53)
collar_s = Suit(19)
pockets_s = Suit(21)
back_s = Suit(78)
sleeves_s = Suit(76)

print(f'Расход ткани на пальто: {collar.consumption + pockets.consumption + back.consumption + sleeves.consumption}.')
print(f'Расход ткани на костюмы: {collar_s.consumption + pockets_s.consumption + back_s.consumption + sleeves_s.consumption}.')
