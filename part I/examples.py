from class_list_of_goods import ListOfGoods
from class_goods import Goods


"""Пример работы с объектом класса Goods"""

print('Создадим объект класса Goods:')
a = Goods('Макароны Макфа 800 г', 34.50, 21)
print(a)

print('\nВыведем имя товара:')
print(a.name_goods)

print('\nПоменяем имя товара:')
a.name_goods = 'Макароны Шебекенские 1 кг'
print(f'Новое имя товара: {a.name_goods}')

print('\nВыведем цену товара:')
print(a.price_goods)

print('\nПоменяем цену товара:')
a.price_goods = 80
print(f'Новая цена товара: {a.price_goods}')

print('\nВыведем количество товара:')
print(a.count_goods)

print('\nПоменяем количество товара:')
a.count_goods = 20
print(f'Новое количество товара: {a.count_goods}')

print('\nПосмотрим на объект класса Goods еще раз:')
print(a)

print('\nОтразим поставку товара в количестве 15 шт:')
print(a.supply_goods(15))

print('\nОтразим продажу товара в количестве 30 шт:')
print(a.sold_goods(30))


"""Пример работы с объектом класса ListOfGoods"""

a = Goods('Макароны Макфа 800 г', 34.50, 21)
b = Goods('Апельсины ЮАР 1 кг', 250, 7)
c = Goods('Сушки маковые 500 г', 70, 10)

print('\nСоздадим объект класса ListOfGoods.')
goods = ListOfGoods()

print('\nДобавим в список товаров объекты класса Goods (a, b, c):')
print(goods.add_goods(a, b, c))

print('\nНайдем все товары в списке, содержащие в Наименовании "мак":')
print(goods.find_goods('мак'))

print('\nВыведем товары с максимальной ценой:')
print(goods.max_price)

print('\nВыведем товары с минимальной ценой:')
print(goods.min_price)

print('\nОтсортируем товары по Наименованию:')
print(goods.sort_goods())

print('\nОтсортируем товары по Цене:')
print(goods.sort_goods('price'))

print('\nОтсортируем товары по Количеству:')
print(goods.sort_goods('count'))

print('\nПоменяем Наименование товара "a":')
print(goods.update_goods('Макароны Макфа 800 г', 'Макароны Мартин 600 г'))

print('\nПоменяем Цену и Количество товара "b":')
print(goods.update_goods('Апельсины ЮАР 1 кг', new_price=230, new_count=5))

print('\nПоменяем Наименование и Количество товара "с":')
print(goods.update_goods('Сушки маковые 500 г', 'Сушки 1 кг', new_count=15))

print('\nОтразим поставку товара "а":')
print(goods.supply_goods('Макароны Мартин 600 г', 5))

print('\nОтразим продажу товара "с":')
print(goods.sold_goods('Сушки 1 кг', 10))

print('\nУдалим товар "a" из списка:')
print(goods.delete_goods('Макароны Мартин 600 г'))

print('\nПосмотрим на список goods еще раз:')
print(goods)
