# GoodsProject

_Практическое задание № 4_

**class_goods.py** - описание и методы класса товара (class Goods)

**class_list_of_goods.py** - описание и методы класса списка товаров (class ListOfGoods)

**examples.py** - примеры работы с классами Goods и ListOfGoods (без вызова исключений)

**unittest_class_list_of_goods.py** - тестирование методов класса ListOfGoods (модуль unittest)

**file_of_goods.py** - создание файла с товарами из списка товаров

**model_goods_sql.py** - описание класса товара Goods в PostgreSQL, описание класса методов работы с товаром в БД GoodsMethods (модуль sqlalchemy)

**view_goods_sql.py** - описание класса ViewGoods, формирующий представление товаров в интерфейсе в результате выполнения запроса

**controller_goods_sql.py** - описание класса ControllerGoods, принимающий запросы в БД от пользователей и возвращающий результат в интерфейсе tkinter. Предусмотрено логгирование операций в файл "log.txt" (модуль logging)

_Для полного представления о функционале программы перед началом работы рекомендуется:_
1. Файлы file_of_goods.py, model_goods_sql.py, view_goods_sql.py, controller_goods_sql.py, goods_image.png сохранить в одной директории;
2. В файле model_goods_sql.py внести персональные данные: username, password - данные для получения доступа к БД, database - название БД в PostgreSQL
3. Запустить файл model_goods_sql.py (для создания таблицы "Goods" в БД)
4. Запустить файл file_of_goods.py для формирования файла с товарами "goods.txt"
5. Запустить файл controller_goods_sql.py: Загрузить из файла -> ввести в поле Файл "goods.txt" -> Ввод
