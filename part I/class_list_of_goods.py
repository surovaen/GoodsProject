from class_goods import Goods


class ListOfGoods:

    """Класс ListOfGoods, формирующий список товаров"""

    def __init__(self):
        self.__list_of_goods = []

    def __str__(self):
        return "\n".join(map(str, self.__list_of_goods))

    @staticmethod
    def __check_goods(value):
        """Проверка аргумента: должен быть объектом Класса Goods"""
        if not isinstance(value, Goods):
            raise ValueError(f'"{value}" не является объектом Класса Goods')

    def add_goods(self, *args):
        """
        Добавление товаров в список

        :param args: товары
        :type args: object of Class Goods

        :return: список товаров
        :rtype: object of Class ListOfGoods
        """
        for goods in args:
            self.__check_goods(goods)
            self.__list_of_goods.append(goods)
            
        return self

    def find_goods(self, value):
        """
        Поиск товаров в списке по Наименованию

        :param value: Наименование товара
        :type value: str

        :return: список найденных товаров
        :rtype: object of Class ListOfGoods
        """
        Goods.check_name(value)

        count = 0
        find_goods_list = ListOfGoods()

        for goods in self.__list_of_goods:
            if value.lower() in goods.name_goods.lower():
                find_goods_list.add_goods(goods)
                count += 1

        if count == 0:
            raise ValueError('Товара нет в списке товаров')

        return f'Найдено {count} товаров\n{find_goods_list}'

    def delete_goods(self, value):
        """
        Удаление товара из списка по Наименованию

        :param value: Наименование товара
        :type value: str

        :return: удаленный товар
        :rtype: object of Class Goods
        """
        Goods.check_name(value)

        for goods in self.__list_of_goods:
            if value.lower() == goods.name_goods.lower():
                self.__list_of_goods.remove(goods)
                break
        else:
            raise ValueError('Товара нет в списке товаров')

        return f'Товар удален из списка\n{goods}'

    @property
    def max_price(self):
        """
        Возвращает список товаров с максимальной ценой

        :return: список товаров с максимальной ценой
        :rtype: object of Class ListOfGoods
        """
        max_price_list = ListOfGoods()
        max_price = max([goods.price_goods for goods in self.__list_of_goods])

        for goods in self.__list_of_goods:
            if goods.price_goods == max_price:
                max_price_list.add_goods(goods)

        return max_price_list

    @property
    def min_price(self):
        """
        Возвращает список товаров с минимальной ценой

        :return: список товаров с минимальной ценой
        :rtype: object of Class ListOfGoods
        """
        min_price_list = ListOfGoods()
        min_price = min([goods.price_goods for goods in self.__list_of_goods])

        for goods in self.__list_of_goods:
            if goods.price_goods == min_price:
                min_price_list.add_goods(goods)

        return min_price_list

    def update_goods(self, value, new_name=None,
                     new_price=None, new_count=None):
        """
        Изменяет данные товара: Наименование, Цена, Количество

        :param value: Наименование товара
        :type value: str

        :param new_name: новое Наименование товара
        :type new_name: str

        :param new_price: новая Цена товара
        :type new_price: int, float

        :param new_count: новое Количество товара
        :type new_count: int

        :return: товар с измененными данными
        :rtype: object of Class Goods
        """
        Goods.check_name(value)

        for goods in self.__list_of_goods:
            if value.lower() == goods.name_goods.lower():
                if new_name is not None:
                    goods.name_goods = new_name
                if new_price is not None:
                    goods.price_goods = new_price
                if new_count is not None:
                    goods.count_goods = new_count
                break
        else:
            raise ValueError('Товара нет в списке товаров')

        return f'Данные по товару изменены\n{goods}'

    def supply_goods(self, value, count):
        """
        Увеличение количества товара с учетом поставки

        :param value: Наименование товара
        :type value: str

        :param count: Количество приобретенного товара
        :type count: int

        :return: товар с измененными данными
        :rtype: object of Class Goods
        """
        Goods.check_name(value)

        for goods in self.__list_of_goods:
            if value.lower() == goods.name_goods.lower():
                goods.supply_goods(count)
                break
        else:
            raise ValueError('Товара нет в списке товаров')

        return f'Поставка товара отражена\n{goods}'

    def sold_goods(self, value, count):
        """
        Уменьшение количества товара с учетом продажи

        :param value: Наименование товара
        :type value: str

        :param count: Количество проданного товара
        :type count: int

        :return: товар с измененными данными
        :rtype: object of Class Goods
        """
        Goods.check_name(value)

        for goods in self.__list_of_goods:
            if value.lower() == goods.name_goods.lower():
                goods.sold_goods(count)
                break
        else:
            raise ValueError('Товара нет в списке товаров')

        return f'Продажа товара отражена\n{goods}'

    def sort_goods(self, sort_key='name'):
        """
        Сортировка списка товаров по Наименованию(по умолчанию)/Цене/Количеству

        :param sort_key: 'name', 'price', 'count'
        :type sort_key:  str

        :return: отсортированный список товаров
        :rtype: object of Class ListOfGoods
        """
        key_functions = {
            'name': lambda x: x.name_goods,
            'price': lambda x: x.price_goods,
            'count': lambda x: x.count_goods
        }

        if sort_key not in key_functions.keys():
            raise KeyError('Сортировка возможна по: '
                           'Наименованию(name)/Цене(price)/Количеству(count)')

        self.__list_of_goods = sorted(self.__list_of_goods,
                                      key=key_functions[sort_key])
        return self
