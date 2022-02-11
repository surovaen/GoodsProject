class ViewGoods:

    """Класс ViewGoods, формирующий представление
    товаров в интерфейс в результате выполнения запроса"""

    @staticmethod
    def show_goods(goods):
        """Представление товарa по запросам:
        Изменение данных, Поставка, Продажа"""
        return f'{goods}\n\nДанные по товару "{goods.name}" обновлены'

    @staticmethod
    def show_all_goods(goods):
        """Представление списка товаров по запросам:
        Показать все товары, Сортировка, Найти товар,
        Макс. товар, Мин. товар, Загрузить из файла"""
        list_of_goods = [f'{line}' for line in goods]
        return '\n'.join(list_of_goods)

    @staticmethod
    def show_add_goods(goods):
        """Представление товарa по запросу Добавить товар"""
        return f'{goods}\n\nТовар "{goods.name}" добавлен в базу данных'

    @staticmethod
    def show_delete_goods(goods):
        """Представление товарa по запросу Удалить товар"""
        return f'{goods}\n\nТовар "{goods.name}" удален из базы данных'
