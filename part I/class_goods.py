class Goods:

    """Класс Goods, описывающий товар,
    принимает параметры: Наименование, Цена, Количество"""

    def __init__(self, name, price=0, count=0):
        self.check_name(name)
        self.__check_price(price)
        self.__check_count(count)

        self.__name = name
        self.__price = price
        self.__count = count

    def __str__(self):
        return f'Наименование: {self.__name}, ' \
               f'Цена: {self.__price}, Количество: ' \
               f'{self.__count}'

    @staticmethod
    def check_name(value):
        """Проверка Наименования товара"""
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError('Наименование должно быть непустой строкой')

    @staticmethod
    def __check_price(value):
        """Проверка Цены товара"""
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError('Цена должна быть неотрицательным числом')

    @staticmethod
    def __check_count(value):
        """Проверка Количества товара"""
        if not isinstance(value, int) or value < 0:
            raise ValueError('Количество должно быть неотрицательным '
                             'целым числом')

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
        self.__check_price(value)
        self.__price = value

    @property
    def count_goods(self):
        return self.__count

    @count_goods.setter
    def count_goods(self, value):
        self.__check_count(value)
        self.__count = value

    def supply_goods(self, value):
        """
        Увеличение количества товара с учетом поставки

        :param value: количество приобретенного товара
        :type value: int

        :return: товар с измененными данными
        :rtype: object of Class Goods
        """
        self.__check_count(value)
        self.count_goods += value
        return self

    def sold_goods(self, value):
        """
        Уменьшение количества товара с учетом продажи

        :param value: количество проданного товара
        :type value: int

        :return: товар с измененными данными
        :rtype: object of Class Goods
        """
        self.__check_count(value)

        if self.count_goods < value:
            raise ValueError(f'Недостаточно {value - self.count_goods} '
                             f'единиц товара на складе')

        self.count_goods -= value
        return self
