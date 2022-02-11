class Goods:

    """Класс Goods, описывающий товар,
    принимает параметры: Наименование, Цена, Количество"""

    @staticmethod
    def check_name(value):
        """Проверка Наименования товара"""
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError('Наименование должно быть непустой строкой')

    @staticmethod
    def check_price(value):
        """Проверка Цены товара"""
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError('Цена должна быть неотрицательным числом')

    @staticmethod
    def check_count(value):
        """Проверка Количества товара"""
        if not isinstance(value, int) or value < 0:
            raise ValueError('Количество должно быть неотрицательным '
                             'целым числом')

    def __init__(self, name, price=0, count=0):
        self.check_name(name)
        self.check_price(price)
        self.check_count(count)

        self.__name = name
        self.__price = price
        self.__count = count

    def __str__(self):
        return f'Наименование: {self.__name}, ' \
               f'Цена: {self.__price}, Количество: ' \
               f'{self.__count}'

    @property
    def name_goods(self):
        return self.__name

    @name_goods.setter
    def name_goods(self, value):
        self.check_name(value)
        self.__name = value

    @property
    def price_goods(self):
        return self.__price

    @price_goods.setter
    def price_goods(self, value):
        self.check_price(value)
        self.__price = value

    @property
    def count_goods(self):
        return self.__count

    @count_goods.setter
    def count_goods(self, value):
        self.check_count(value)
        self.__count = value

    def supply(self, value):
        """
        Увеличение количества товара с учетом поставки

        :param value: количество приобретенного товара
        :type value: int

        :return: товар с измененными данными
        :rtype: object of Class Goods
        """
        self.check_count(value)
        self.count_goods += value
        return self

    def sold(self, value):
        """
        Уменьшение количества товара с учетом продажи

        :param value: количество проданного товара
        :type value: int

        :return: товар с измененными данными
        :rtype: object of Class Goods
        """
        self.check_count(value)

        if self.count_goods < value:
            raise ValueError(f'Недостаточно {value - self.count_goods} '
                             f'единиц товара на складе')

        self.count_goods -= value
        return self
