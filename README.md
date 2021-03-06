# GoodsProject

_Практическое задание № 4_

### PART I - работа с классами, тестирование класса (модуль unittest)
- **class_goods.py** - описание и методы класса товара Goods

- **class_list_of_goods.py** - описание и методы класса списка товаров ListOfGoods

- **examples.py** - примеры работы с классами Goods и ListOfGoods (без вызова исключений)

- **unittest_class_list_of_goods.py** - тестирование методов класса ListOfGoods

- **file_of_goods.py** - создание файла с товарами из списка товаров

### PART II - создание пользовательского интерфейса (модуль tkinter) взаимодействия с базой данных, реализация паттерна MVC

- **model_goods_sql.py** - описание класса товара Goods в PostgreSQL, описание класса методов работы с товаром GoodsMethods в БД (модуль sqlalchemy)

- **view_goods_sql.py** - описание класса ViewGoods, формирующего представление товаров в интерфейсе в результате выполнения запроса; описание классa Interface - пользовательский интерфейс (модуль tkinter)

- **controller_goods_sql.py** - описание класса ControllerGoods, принимающего запросы в БД от пользователей и возвращающего результат в интерфейс; описание класса CheckParameter, проверящего введенные пользователем параметры. Предусмотрено логгирование операций пользователя в файл "log.txt" (модуль logging)

_Для полного представления о функционале программы перед началом работы:_
1. Файлы в "path II" сохранить в одной директории;
2. В файле model_goods_sql.py внести персональные данные: username, password - данные для получения доступа к БД, database - название БД в PostgreSQL
3. Запустить файл model_goods_sql.py (для создания таблицы "Goods" в БД)
4. Запустить файл controller_goods_sql.py: Загрузить из файла -> ввести в поле Файл "goods.txt" -> Ввод

_Пользовательский интерфейс:_
![image](https://user-images.githubusercontent.com/94726007/154430741-b4456016-aac7-410f-80ce-9d39ab7eb2e1.png)
