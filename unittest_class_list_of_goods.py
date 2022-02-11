from class_goods import Goods
from class_list_of_goods import ListOfGoods
import unittest


class TestListOfGoodsMethods(unittest.TestCase):
    def setUp(self):
        self.a = Goods('Макароны Макфа 800 г', 34.50, 21)
        self.b = Goods('Колбаса Мираторг 300 г', 345, 17)
        self.c = Goods('Сыр Маасдам 250 г', 345, 4)
        self.d = Goods('Апельсины ЮАР 1 кг', 204.70, 6)
        self.e = Goods('Хлеб Бородинский 300 г', 34.50, 30)
        self.f = Goods('Чай Майский 100 г', 54, 29)
        self.test_list = ListOfGoods()
        self.test_list.add_goods(
                self.a, self.b, self.c,
                self.d, self.e, self.f
        )

    def test_max_price(self):
        """Тест товаров с максимальной ценой"""
        max_test_list = ListOfGoods()
        max_test_list.add_goods(self.b, self.c)
        self.assertEqual(str(self.test_list.max_price), str(max_test_list))

    def test_min_price(self):
        """Тест товаров с минимальной ценой"""
        min_test_list = ListOfGoods()
        min_test_list.add_goods(self.a, self.e)
        self.assertEqual(str(self.test_list.min_price), str(min_test_list))

    def test_sort_name(self):
        """Тест сортировки по Наименованию товара"""
        name_list = ListOfGoods()
        name_list.add_goods(
                self.d, self.b, self.a,
                self.c, self.e, self.f
        )
        self.assertEqual(str(self.test_list.sort_goods()), str(name_list))

    def test_sort_price(self):
        """Тест сортировки по Цене товара"""
        price_list = ListOfGoods()
        price_list.add_goods(
                self.a, self.e, self.f,
                self.d, self.b, self.c
        )
        self.assertEqual(
                str(self.test_list.sort_goods('price')),
                str(price_list)
        )

    def test_sort_count(self):
        """Тест сортировки по Количеству товара"""
        count_list = ListOfGoods()
        count_list.add_goods(
                self.c, self.d, self.b,
                self.a, self.f, self.e
        )
        self.assertEqual(
                str(self.test_list.sort_goods('count')),
                str(count_list))


if __name__ == '__main__':
    unittest.main()
