from model_goods_sql import GoodsMethods
from tkinter import scrolledtext, messagebox
from view_goods_sql import ViewGoods
import logging as log
import tkinter as tk


FORMAT = '%(asctime)s - in %(filename)s: ' \
         'level %(levelname)s in %(funcName)s - %(message)s'
log.basicConfig(filename="log.txt", level=log.INFO, format=FORMAT)


class ControllerGoods:

    """Класс ControllerGoods, связывающий запросы
    на работу с БД в интерфейсе c представлением"""

    # переменная func_btn_name (имя кнопки)
    # переопределяется в функциях запросов при нажатии соответствующих кнопок
    func_btn_name = ''

    # переменная check_status (проверка True/False)
    # переопределяется при выполнении функций check
    check_status = None

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
        """Все товары из БД"""
        log.info('Показать все товары')
        ControllerGoods.disabled()
        goods.config(state=tk.NORMAL)
        goods.delete(1.0, tk.END)

        out_info = GoodsMethods.show_all()
        goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def max_price_goods():
        """Товары с максимальной ценой"""
        log.info('Макс. цена')
        ControllerGoods.disabled()
        goods.config(state=tk.NORMAL)
        goods.delete(1.0, tk.END)

        out_info = GoodsMethods.max_price_goods()
        goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def min_price_goods():
        """Товары с минимальной ценой"""
        log.info('Мин. цена')
        ControllerGoods.disabled()
        goods.config(state=tk.NORMAL)
        goods.delete(1.0, tk.END)

        out_info = GoodsMethods.min_price_goods()
        goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def sort_name():
        """Сортировка товаров по Наименованию"""
        log.info('Сортировка по Наименованию')
        ControllerGoods.disabled()
        goods.config(state=tk.NORMAL)
        goods.delete(1.0, tk.END)

        out_info = GoodsMethods.sort_name_goods()
        goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def sort_price():
        """Сортировка товаров по Цене"""
        log.info('Сортировка по Цене')
        ControllerGoods.disabled()
        goods.config(state=tk.NORMAL)
        goods.delete(1.0, tk.END)

        out_info = GoodsMethods.sort_price_goods()
        goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def sort_count():
        """Сортировка товаров по Количеству"""
        log.info('Сортировка по Количеству')
        ControllerGoods.disabled()
        goods.config(state=tk.NORMAL)
        goods.delete(1.0, tk.END)

        out_info = GoodsMethods.sort_count_goods()
        goods.insert(tk.INSERT, ViewGoods.show_all_goods(out_info))

    @staticmethod
    def from_file():
        """Добавление товаров в БД из файла

        Активирует виджеты из списка from_file_list"""
        log.info('Загрузить из файла')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(from_file_list)

        ControllerGoods.func_btn_name = 'from_file'

    @staticmethod
    def find_goods():
        """Поиск товара по Наименованию

        Активирует виджеты из списка find_del_list"""
        log.info('Найти товар')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(find_del_list)

        ControllerGoods.func_btn_name = 'find_goods'

    @staticmethod
    def add_goods():
        """Добавление товара в БД

        Активирует виджеты из списка add_upd_list"""
        log.info('Добавить товар')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(add_upd_list)

        ControllerGoods.func_btn_name = 'add_goods'

    @staticmethod
    def upd_goods():
        """Изменение Цены, Количества товара в БД

        Активирует виджеты из списка add_upd_list"""
        log.info('Изменить данные')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(add_upd_list)

        ControllerGoods.func_btn_name = 'upd_goods'

    @staticmethod
    def del_goods():
        """Удаление товара из БД

        Активирует виджеты из списка find_del_list"""
        log.info('Удалить товар')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(find_del_list)

        ControllerGoods.func_btn_name = 'del_goods'

    @staticmethod
    def sup_goods():
        """Поставка количества товара

        Активирует виджеты из списка sup_sold_list"""
        log.info('Продажа')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(sup_sold_list)

        ControllerGoods.func_btn_name = 'sup_goods'

    @staticmethod
    def sold_goods():
        """Продажа товара

        Активирует виджеты из списка sup_sold_list"""
        log.info('Покупка')
        ControllerGoods.disabled()
        ControllerGoods.normal_state(sup_sold_list)

        ControllerGoods.func_btn_name = 'sold_goods'

    @staticmethod
    def check_name(value):
        """Проверка Наименования товара"""
        if value == '':
            messagebox.showwarning('Ошибка',
                                   'Введите наименование товара')
            log.error('Пустая строка')
            ControllerGoods.check_status = False

    @staticmethod
    def check_price(value):
        """Проверка Цены товара"""
        if value == '':
            messagebox.showwarning('Ошибка',
                                   'Введите цену товара')
            log.error('Пустая строка')
            ControllerGoods.check_status = False
        else:
            try:
                int(value)
            except ValueError:
                messagebox.showwarning('Ошибка',
                                       'Цена должна быть числом')
                log.error('Цена: введено не число')
                ControllerGoods.check_status = False

    @staticmethod
    def check_count(value):
        """Проверка Количества товара"""
        if value == '':
            messagebox.showwarning('Ошибка',
                                   'Введите количество товара')
            log.error('Пустая строка')
            ControllerGoods.check_status = False
        else:
            try:
                int(value)
            except ValueError:
                messagebox.showwarning('Ошибка',
                                       'Количество должно быть числом')
                log.error('Количество: введено не число')
                ControllerGoods.check_status = False

    @staticmethod
    def check_file(value):
        """Проверка имени файла"""
        if value == '':
            messagebox.showwarning('Ошибка',
                                   'Введите имя файла')
            log.error('Пустая строка')
            ControllerGoods.check_status = False

    @staticmethod
    def check_update(value1, value2):
        """Проверка Цены/Количества изменяемого товара"""
        if value1 == '' and value2 == '':
            messagebox.showwarning('Ошибка',
                                   'Введите цену и/или количество товара')
            log.error('Пустая строка')
            ControllerGoods.check_status = False

        if value1 != '':
            try:
                int(value1)
            except ValueError:
                messagebox.showwarning('Ошибка',
                                       'Цена должнa быть числом')
                log.error('Цена: введено не число')
                ControllerGoods.check_status = False

        if value2 != '':
            try:
                int(value2)
            except ValueError:
                messagebox.showwarning('Ошибка',
                                       'Количество должно быть числом')
                log.error('Количество: введено не число')
                ControllerGoods.check_status = False

    @staticmethod
    def execution_function():
        """Выполнение запросов на основе полученных данных"""
        name_goods = input_name.get()
        price_goods = input_price.get()
        count_goods = input_count.get()
        file_goods = input_file.get()
        ControllerGoods.check_status = True

        ControllerGoods.delete_all()
        goods.delete(1.0, tk.END)

        if ControllerGoods.func_btn_name == 'find_goods':
            ControllerGoods.check_name(name_goods)
            if ControllerGoods.check_status:
                try:
                    out = GoodsMethods.find_goods(name_goods)
                except ValueError:
                    goods.insert(tk.INSERT,
                                 f'Товара "{name_goods}" нет в базе данных')
                    log.error('Товар отсутствует в БД')
                else:
                    goods.insert(tk.INSERT,
                                 ViewGoods.show_all_goods(out))
                    log.info('Успешно')

        if ControllerGoods.func_btn_name == 'from_file':
            ControllerGoods.check_file(file_goods)
            if ControllerGoods.check_status:
                try:
                    out = GoodsMethods.create_goods_from_file(file_goods)
                except FileNotFoundError:
                    messagebox.showinfo('Внимание',
                                        f'Файл "{file_goods}" не найден')
                    log.error('Некорректное имя файла')
                else:
                    goods.insert(tk.INSERT,
                                 ViewGoods.show_all_goods(out))
                    log.info('Успешно')

        if ControllerGoods.func_btn_name == 'add_goods':
            ControllerGoods.check_name(name_goods)
            ControllerGoods.check_price(price_goods)
            ControllerGoods.check_count(count_goods)
            if ControllerGoods.check_status:
                try:
                    out = GoodsMethods.add_goods(name_goods,
                                                 price_goods,
                                                 count_goods)
                except ValueError:
                    goods.insert(tk.INSERT,
                                 f'Товар "{name_goods}" есть в базе данных')
                    log.error('Товар уже есть в БД')
                else:
                    goods.insert(tk.INSERT,
                                 ViewGoods.show_add_goods(out))
                    log.info('Успешно')

        if ControllerGoods.func_btn_name == 'del_goods':
            ControllerGoods.check_name(name_goods)
            if ControllerGoods.check_status:
                try:
                    out = GoodsMethods.delete_goods(name_goods)
                except ValueError:
                    goods.insert(tk.INSERT,
                                 f'Товара "{name_goods}" нет в базе данных')
                    log.error('Товар отсутствует в БД')
                else:
                    goods.insert(tk.INSERT,
                                 ViewGoods.show_delete_goods(out))
                    log.info('Успешно')

        if ControllerGoods.func_btn_name == 'upd_goods':
            ControllerGoods.check_name(name_goods)
            ControllerGoods.check_update(price_goods, count_goods)
            if ControllerGoods.check_status:
                try:
                    out = GoodsMethods.update_goods(name_goods,
                                                    price_goods,
                                                    count_goods)
                except ValueError:
                    goods.insert(tk.INSERT,
                                 f'Товара "{name_goods}" нет в базе данных')
                    log.error('Товар отсутствует в БД')
                else:
                    goods.insert(tk.INSERT,
                                 ViewGoods.show_goods(out))
                    log.info('Успешно')

        if ControllerGoods.func_btn_name == 'sup_goods':
            ControllerGoods.check_name(name_goods)
            ControllerGoods.check_count(count_goods)
            if ControllerGoods.check_status:
                try:
                    out = GoodsMethods.supply_goods(name_goods, count_goods)
                except ValueError:
                    goods.insert(tk.INSERT,
                                 f'Товара "{name_goods}" нет в базе данных')
                    log.error('Товар отсутствует в БД')
                else:
                    goods.insert(tk.INSERT,
                                 ViewGoods.show_goods(out))
                    log.info('Успешно')

        if ControllerGoods.func_btn_name == 'sold_goods':
            ControllerGoods.check_name(name_goods)
            ControllerGoods.check_count(count_goods)
            if ControllerGoods.check_status:
                try:
                    out = GoodsMethods.sold_goods(name_goods, count_goods)
                except ValueError:
                    goods.insert(tk.INSERT,
                                 f'Товара "{name_goods}" нет в базе данных')
                    log.error('Товар отсутствует в БД')
                except OverflowError:
                    goods.insert(tk.INSERT,
                                 f'Недостаточно товара "{name_goods}"')
                    log.error('Недостаточно товара на складе')
                else:
                    goods.insert(tk.INSERT,
                                 ViewGoods.show_goods(out))
                    log.info('Успешно')

        ControllerGoods.disabled()


"""WINDOW"""
main_win = tk.Tk()
main_win.geometry('800x655+100+100')
main_win.title('БД Товары')
photo = tk.PhotoImage(file='goods_image.png')
main_win.iconphoto(False, photo)
main_win.resizable(False, False)
main_win.columnconfigure(0, minsize=200)
main_win.columnconfigure(1, minsize=200)
main_win.columnconfigure(2, minsize=150)
main_win.columnconfigure(3, minsize=250)

"""BUTTONS"""
find_btn = tk.Button(main_win, text='Найти товар',
                     command=ControllerGoods.find_goods,
                     activebackground='grey', bg='#FFFFFF')
add_btn = tk.Button(main_win, text='Добавить товар',
                    command=ControllerGoods.add_goods,
                    activebackground='grey', bg='#FFFFFF')
file_btn = tk.Button(main_win, text='Загрузить из файла',
                     command=ControllerGoods.from_file,
                     activebackground='grey', bg='#FFFFFF')
upd_btn = tk.Button(main_win, text='Изменить данные',
                    command=ControllerGoods.upd_goods,
                    activebackground='grey', bg='#FFFFFF')
del_btn = tk.Button(main_win, text='Удалить товар',
                    command=ControllerGoods.del_goods,
                    activebackground='grey', bg='#FFFFFF')
sup_btn = tk.Button(main_win, text='Поставка ',
                    command=ControllerGoods.sup_goods,
                    activebackground='grey', bg='#FFFFFF')
sold_btn = tk.Button(main_win, text='Продажа',
                     command=ControllerGoods.sold_goods,
                     activebackground='grey', bg='#FFFFFF')
max_pr_btn = tk.Button(main_win, text='Макс. цена',
                       command=ControllerGoods.max_price_goods,
                       activebackground='grey', bg='#E5E5E5')
min_pr_btn = tk.Button(main_win, text='Мин. цена',
                       command=ControllerGoods.min_price_goods,
                       activebackground='grey', bg='#E5E5E5')
name_s_btn = tk.Button(main_win, text='по имени',
                       command=ControllerGoods.sort_name,
                       activebackground='grey', bg='#E5E5E5')
price_s_btn = tk.Button(main_win, text='по цене',
                        command=ControllerGoods.sort_price,
                        activebackground='grey', bg='#E5E5E5')
count_s_btn = tk.Button(main_win, text='по количеству',
                        command=ControllerGoods.sort_count,
                        activebackground='grey', bg='#E5E5E5')
all_btn = tk.Button(main_win, text='Показать все товары',
                    command=ControllerGoods.show_all,
                    activebackground='grey', bg='#E5E5E5')
get_btn = tk.Button(main_win, text='Ввод',
                    command=ControllerGoods.execution_function,
                    activebackground='grey', state=tk.DISABLED)

add_btn.grid(row=3, column=0, stick='we')
find_btn.grid(row=2, column=0, stick='we')
file_btn.grid(row=6, column=2, columnspan=2, stick='we')
upd_btn.grid(row=4, column=0, stick='we')
del_btn.grid(row=5, column=0, stick='we')
sup_btn.grid(row=4, column=1, stick='we')
sold_btn.grid(row=5, column=1, stick='we')
max_pr_btn.grid(row=6, column=0, stick='we')
min_pr_btn.grid(row=6, column=1, stick='we')
name_s_btn.grid(row=1, column=1, stick='we')
price_s_btn.grid(row=2, column=1, stick='we')
count_s_btn.grid(row=3, column=1, stick='we')
all_btn.grid(row=0, column=0, rowspan=2, stick='wens')
get_btn.grid(row=4, column=2, rowspan=2, columnspan=2, stick='wens')

"""LABELS, ENTRY"""
sort_label = tk.Label(main_win, text='Сортировка:',
                      font=('@Microsoft JhengHei UI', 10))
name_label = tk.Label(main_win, text='Наименование', state=tk.DISABLED,
                      font=('@Microsoft JhengHei UI', 10))
price_label = tk.Label(main_win, text='Цена', state=tk.DISABLED,
                       font=('@Microsoft JhengHei UI', 10))
count_label = tk.Label(main_win, text='Количество', state=tk.DISABLED,
                       font=('@Microsoft JhengHei UI', 10))
file_label = tk.Label(main_win, text='Файл', state=tk.DISABLED,
                      font=('@Microsoft JhengHei UI', 10))
name_goods_label = tk.Label(main_win, text='Наименование',
                            font=('@Microsoft JhengHei UI', 10))
price_goods_label = tk.Label(main_win, text='Цена',
                             font=('@Microsoft JhengHei UI', 10))
count_goods_label = tk.Label(main_win, text='Количество',
                             font=('@Microsoft JhengHei UI', 10))

sort_label.grid(row=0, column=1)
name_label.grid(row=0, column=2)
price_label.grid(row=1, column=2)
count_label.grid(row=2, column=2)
file_label.grid(row=3, column=2)
name_goods_label.grid(row=7, column=0, columnspan=2)
price_goods_label.grid(row=7, column=2)
count_goods_label.grid(row=7, column=3)

"""ENTRIES"""
input_name = tk.Entry(main_win, state=tk.DISABLED)
input_price = tk.Entry(main_win, state=tk.DISABLED)
input_count = tk.Entry(main_win, state=tk.DISABLED)
input_file = tk.Entry(main_win, state=tk.DISABLED)

input_name.grid(row=0, column=3, stick='we')
input_price.grid(row=1, column=3, stick='we')
input_count.grid(row=2, column=3, stick='we')
input_file.grid(row=3, column=3, stick='we')

goods = scrolledtext.ScrolledText(main_win, width=40,
                                  height=30, state=tk.DISABLED,
                                  font=('Lucida Console', 11))
goods.grid(row=8, column=0, columnspan=7, stick='wens')

"""LISTS"""
delete_list = [
    input_name,
    input_price,
    input_count,
    input_file
]

from_file_list = [
    get_btn,
    file_label,
    input_file,
    goods
]

disabled_list = [
    get_btn,
    name_label,
    input_name,
    price_label,
    input_price,
    count_label,
    input_count,
    file_label,
    input_file,
    goods
]

find_del_list = [
    get_btn,
    input_name,
    name_label,
    goods
]

add_upd_list = [
    get_btn,
    name_label,
    price_label,
    count_label,
    goods,
    input_name,
    input_price,
    input_count
]

sup_sold_list = [
    get_btn,
    name_label,
    count_label,
    input_name,
    input_count,
    goods
]

if __name__ == '__main__':
    log.info('Запуск программы')
    main_win.mainloop()
