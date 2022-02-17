from model_goods_sql import GoodsMethods
from tkinter import messagebox
from view_goods_sql import ViewGoods, Interface
import logging as log
import tkinter as tk

FORMAT = '%(asctime)s - in %(filename)s: ' \
         'level %(levelname)s in %(funcName)s - %(message)s'
log.basicConfig(filename="../log.txt", level=log.INFO, format=FORMAT)


class CheckParameter:
    """Класс CheckParameter, описывающий методы проверки параметров товара"""

    # переменная check_status (проверка True/False)
    # переопределяется при выполнении функций CheckParameter
    check_status = None

    @staticmethod
    def check_name(value):
        """Проверка Наименования товара"""
        if value == '':
            messagebox.showwarning('Ошибка', 'Введите наименование товара')
            log.error('Наименование: Пустая строка')
            CheckParameter.check_status = False

    @staticmethod
    def check_price(value):
        """Проверка Цены товара"""
        if value == '':
            messagebox.showwarning('Ошибка', 'Введите цену товара')
            log.error('Цена: Пустая строка')
            CheckParameter.check_status = False
        else:
            try:
                int(value)
            except ValueError:
                messagebox.showwarning('Ошибка', 'Цена должна быть числом')
                log.error('Цена: Введено не число')
                CheckParameter.check_status = False

    @staticmethod
    def check_count(value):
        """Проверка Количества товара"""
        if value == '':
            messagebox.showwarning('Ошибка', 'Введите количество товара')
            log.error('Количество: Пустая строка')
            CheckParameter.check_status = False
        else:
            try:
                int(value)
            except ValueError:
                messagebox.showwarning('Ошибка',
                                       'Количество должно быть числом')
                log.error('Количество: Введено не число')
                CheckParameter.check_status = False

    @staticmethod
    def check_file(value):
        """Проверка имени файла"""
        if value == '':
            messagebox.showwarning('Ошибка', 'Введите имя файла')
            log.error('Файл: Пустая строка')
            CheckParameter.check_status = False

    @staticmethod
    def check_update(value1, value2):
        """Проверка Цены/Количества изменяемого товара"""
        if value1 == '' and value2 == '':
            messagebox.showwarning('Ошибка',
                                   'Введите цену и/или количество товара')
            log.error('Цена/Количество: Пустая строка')
            CheckParameter.check_status = False

        if value1 != '':
            try:
                int(value1)
            except ValueError:
                messagebox.showwarning('Ошибка', 'Цена должнa быть числом')
                log.error('Цена: введено не число')
                CheckParameter.check_status = False

        if value2 != '':
            try:
                int(value2)
            except ValueError:
                messagebox.showwarning('Ошибка',
                                       'Количество должно быть числом')
                log.error('Количество: введено не число')
                CheckParameter.check_status = False


# создание объекта Класса Interface
win = Interface()


class ControllerGoods:
    """Класс ControllerGoods, связывающий запросы
    на работу с БД в интерфейсе c представлением"""

    # переменная func_btn_name (имя кнопки)
    # переопределяется в функциях запросов при нажатии соответствующих кнопок
    func_btn_name = ''

    @staticmethod
    def disabled():
        """Отключает неиспользуемые виджеты в списке disabled_list"""
        return list(map(lambda x: x.config(state=tk.DISABLED), disabled_list))

    @staticmethod
    def delete_all():
        """Очищает виджеты в списке delete_list"""
        list(map(lambda x: x.delete(0, tk.END), delete_list))

    @staticmethod
    def normal_state(normal_list):
        """Включает используемые виджеты в списке normal_list (опционально)"""
        return list(map(lambda x: x.config(state=tk.NORMAL), normal_list))

    @staticmethod
    def show_all():
        """Показать все товары из БД"""
        log.info('Показать все товары')
        ControllerGoods.disabled()
        win.goods.config(state=tk.NORMAL)
        win.goods.delete(1.0, tk.END)

        out_info = GoodsMethods.show_all()
        win.goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def max_price_goods():
        """Товары с максимальной ценой"""
        log.info('Макс. цена')
        ControllerGoods.disabled()
        win.goods.config(state=tk.NORMAL)
        win.goods.delete(1.0, tk.END)

        out_info = GoodsMethods.max_price_goods()
        win.goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def min_price_goods():
        """Товары с минимальной ценой"""
        log.info('Мин. цена')
        ControllerGoods.disabled()
        win.goods.config(state=tk.NORMAL)
        win.goods.delete(1.0, tk.END)

        out_info = GoodsMethods.min_price_goods()
        win.goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def sort_name():
        """Сортировка товаров по Наименованию"""
        log.info('Сортировка по Наименованию')
        ControllerGoods.disabled()
        win.goods.config(state=tk.NORMAL)
        win.goods.delete(1.0, tk.END)

        out_info = GoodsMethods.sort_name_goods()
        win.goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def sort_price():
        """Сортировка товаров по Цене"""
        log.info('Сортировка по Цене')
        ControllerGoods.disabled()
        win.goods.config(state=tk.NORMAL)
        win.goods.delete(1.0, tk.END)

        out_info = GoodsMethods.sort_price_goods()
        win.goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def sort_count():
        """Сортировка товаров по Количеству"""
        log.info('Сортировка по Количеству')
        ControllerGoods.disabled()
        win.goods.config(state=tk.NORMAL)
        win.goods.delete(1.0, tk.END)

        out_info = GoodsMethods.sort_count_goods()
        win.goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def from_file():
        """Загрузить товары в БД из файла

        Активирует виджеты из списка from_file_list"""
        log.info('Загрузить из файла')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(from_file_list)

        ControllerGoods.func_btn_name = 'from_file'

    @staticmethod
    def download(param_list):
        """
        Функция загрузки товаров из файла

        :param param_list: список параметров
        :type param_list: list
        """
        *args, file_goods = param_list
        CheckParameter.check_file(file_goods)

        if CheckParameter.check_status:
            try:
                out = GoodsMethods.create_goods_from_file(file_goods)
            except FileNotFoundError:
                messagebox.showinfo('Внимание',
                                    f'Файл "{file_goods}" не найден')
                log.error('Некорректное имя файла')
            else:
                win.goods.insert(tk.INSERT, ViewGoods.show_all_goods(out))
                log.info('Загрузка: Успешно')

    @staticmethod
    def find_goods():
        """Найти товар по Наименованию

        Активирует виджеты из списка find_del_list"""
        log.info('Найти товар')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(find_del_list)

        ControllerGoods.func_btn_name = 'find_goods'

    @staticmethod
    def finding(param_list):
        """
        Функция поиска товара по Наименованию

        :param param_list: список параметров
        :type param_list: list
        """
        name_goods, *args = param_list
        CheckParameter.check_name(name_goods)

        if CheckParameter.check_status:
            try:
                out = GoodsMethods.find_goods(name_goods)
            except ValueError:
                win.goods.insert(tk.INSERT,
                                 f'Товара "{name_goods}" нет в базе данных')
                log.error('Товар отсутствует в БД')
            else:
                win.goods.insert(tk.INSERT, ViewGoods.show_all_goods(out))
                log.info('Поиск: Успешно')

    @staticmethod
    def add_goods():
        """Добавить товар в БД

        Активирует виджеты из списка add_upd_list"""
        log.info('Добавить товар')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(add_upd_list)

        ControllerGoods.func_btn_name = 'add_goods'

    @staticmethod
    def adding(param_list):
        """
        Функция добавления товара в БД

        :param param_list: список параметров
        :type param_list: list
        """
        name_goods, price_goods, count_goods, _ = param_list
        CheckParameter.check_name(name_goods)
        CheckParameter.check_price(price_goods)
        CheckParameter.check_count(count_goods)

        if CheckParameter.check_status:
            try:
                out = GoodsMethods.add_goods(name_goods, price_goods,
                                             count_goods)
            except ValueError:
                win.goods.insert(tk.INSERT,
                                 f'Товар "{name_goods}" есть в базе данных')
                log.error('Товар уже есть в БД')
            else:
                win.goods.insert(tk.INSERT, ViewGoods.show_add_goods(out))
                log.info('Добавление: Успешно')

    @staticmethod
    def upd_goods():
        """Изменение Цены, Количества товара в БД

        Активирует виджеты из списка add_upd_list"""
        log.info('Изменить данные')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(add_upd_list)

        ControllerGoods.func_btn_name = 'upd_goods'

    @staticmethod
    def update(param_list):
        """
        Функция изменения Цены и/или Количества товара

        :param param_list: список параметров
        :type param_list: list
        """
        name_goods, price_goods, count_goods, _ = param_list
        CheckParameter.check_name(name_goods)
        CheckParameter.check_update(price_goods, count_goods)

        if CheckParameter.check_status:
            try:
                out = GoodsMethods.update_goods(name_goods, price_goods,
                                                count_goods)
            except ValueError:
                win.goods.insert(tk.INSERT,
                                 f'Товара "{name_goods}" нет в базе данных')
                log.error('Товар отсутствует в БД')
            else:
                win.goods.insert(tk.INSERT, ViewGoods.show_goods(out))
                log.info('Изменение: Успешно')

    @staticmethod
    def del_goods():
        """Удалить товар из БД

        Активирует виджеты из списка find_del_list"""
        log.info('Удалить товар')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(find_del_list)

        ControllerGoods.func_btn_name = 'del_goods'

    @staticmethod
    def removal(param_list):
        """
        Функция удаления товара из БД

        :param param_list: список параметров
        :type param_list: list
        """
        name_goods, *args = param_list
        CheckParameter.check_name(name_goods)

        if CheckParameter.check_status:
            try:
                out = GoodsMethods.delete_goods(name_goods)
            except ValueError:
                win.goods.insert(tk.INSERT,
                                 f'Товара "{name_goods}" нет в базе данных')
                log.error('Товар отсутствует в БД')
            else:
                win.goods.insert(tk.INSERT, ViewGoods.show_delete_goods(out))
                log.info('Обновление: Успешно')

    @staticmethod
    def sup_goods():
        """Поставка количества товара

        Активирует виджеты из списка sup_sold_list"""
        log.info('Продажа')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(sup_sold_list)

        ControllerGoods.func_btn_name = 'sup_goods'

    @staticmethod
    def supply(param_list):
        """
        Функция отражения поставки товара

        :param param_list: список параметров
        :type param_list: list
        """
        name_goods, _, count_goods, _ = param_list
        CheckParameter.check_name(name_goods)
        CheckParameter.check_count(count_goods)

        if CheckParameter.check_status:
            try:
                out = GoodsMethods.supply_goods(name_goods, count_goods)
            except ValueError:
                win.goods.insert(tk.INSERT,
                                 f'Товара "{name_goods}" нет в базе данных')
                log.error('Товар отсутствует в БД')
            else:
                win.goods.insert(tk.INSERT, ViewGoods.show_goods(out))
                log.info('Поставка: Успешно')

    @staticmethod
    def sold_goods():
        """Продажа товара

        Активирует виджеты из списка sup_sold_list"""
        log.info('Покупка')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(sup_sold_list)

        ControllerGoods.func_btn_name = 'sold_goods'

    @staticmethod
    def sold(param_list):
        """
        Функция отражения продажи товара

        :param param_list: список параметров
        :type param_list: list
        """
        name_goods, _, count_goods, _ = param_list
        CheckParameter.check_name(name_goods)
        CheckParameter.check_count(count_goods)

        if CheckParameter.check_status:
            try:
                out = GoodsMethods.sold_goods(name_goods, count_goods)
            except ValueError:
                win.goods.insert(tk.INSERT,
                                 f'Товара "{name_goods}" нет в базе данных')
                log.error('Товар отсутствует в БД')
            except OverflowError:
                win.goods.insert(tk.INSERT,
                                 f'Недостаточно товара "{name_goods}"')
                log.error('Недостаточно товара на складе')
            else:
                win.goods.insert(tk.INSERT, ViewGoods.show_goods(out))
                log.info('Продажа: Успешно')

    @staticmethod
    def execution_function():
        """Выполнение функций на основе полученных данных"""
        name_goods = win.input_name.get()
        price_goods = win.input_price.get()
        count_goods = win.input_count.get()
        file_goods = win.input_file.get()
        param_list = [name_goods, price_goods, count_goods, file_goods]

        CheckParameter.check_status = True
        ControllerGoods.delete_all()
        win.goods.delete(1.0, tk.END)

        functions = {
            'find_goods': ControllerGoods.finding,
            'from_file': ControllerGoods.download,
            'add_goods': ControllerGoods.adding,
            'del_goods': ControllerGoods.removal,
            'upd_goods': ControllerGoods.update,
            'sup_goods': ControllerGoods.supply,
            'sold_goods': ControllerGoods.sold
        }

        functions[ControllerGoods.func_btn_name](param_list)
        ControllerGoods.disabled()


# присвоение функций кнопкам интерфейса
win.find_btn.config(command=ControllerGoods.find_goods)
win.add_btn.config(command=ControllerGoods.add_goods)
win.file_btn.config(command=ControllerGoods.from_file)
win.upd_btn.config(command=ControllerGoods.upd_goods)
win.del_btn.config(command=ControllerGoods.del_goods)
win.sup_btn.config(command=ControllerGoods.sup_goods)
win.sold_btn.config(command=ControllerGoods.sold_goods)
win.max_pr_btn.config(command=ControllerGoods.max_price_goods)
win.min_pr_btn.config(command=ControllerGoods.min_price_goods)
win.name_s_btn.config(command=ControllerGoods.sort_name)
win.price_s_btn.config(command=ControllerGoods.sort_price)
win.count_s_btn.config(command=ControllerGoods.sort_count)
win.all_btn.config(command=ControllerGoods.show_all)
win.get_btn.config(command=ControllerGoods.execution_function)

"""LISTS"""

delete_list = [
    win.input_name,
    win.input_price,
    win.input_count,
    win.input_file
]

from_file_list = [
    win.get_btn,
    win.file_lbl,
    win.input_file,
    win.goods
]

disabled_list = [
    win.get_btn,
    win.name_lbl,
    win.input_name,
    win.price_lbl,
    win.input_price,
    win.count_lbl,
    win.input_count,
    win.file_lbl,
    win.input_file,
    win.goods
]

find_del_list = [
    win.get_btn,
    win.input_name,
    win.name_lbl,
    win.goods
]

add_upd_list = [
    win.get_btn,
    win.name_lbl,
    win.price_lbl,
    win.count_lbl,
    win.goods,
    win.input_name,
    win.input_price,
    win.input_count
]

sup_sold_list = [
    win.get_btn,
    win.name_lbl,
    win.count_lbl,
    win.input_name,
    win.input_count,
    win.goods
]

if __name__ == '__main__':
    log.info('Запуск программы')
    win.mainloop()
