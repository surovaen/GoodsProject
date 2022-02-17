from tkinter import scrolledtext
import tkinter as tk


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


class Interface(tk.Tk):

    """Пользовательский интерфейс работы с БД"""

    def __init__(self):
        super().__init__()

        self.geometry('800x655+100+100')
        self.title('БД Товары')
        photo = tk.PhotoImage(file='goods_image.png')
        self.iconphoto(False, photo)
        self.resizable(False, False)
        self.columnconfigure(0, minsize=200)
        self.columnconfigure(1, minsize=200)
        self.columnconfigure(2, minsize=150)
        self.columnconfigure(3, minsize=250)

        self.find_btn = tk.Button(self, text='Найти товар',
                                  activebackground='grey', bg='#E5E5E5')
        self.add_btn = tk.Button(self, text='Добавить товар',
                                 activebackground='grey', bg='#E5E5E5')
        self.file_btn = tk.Button(self, text='Загрузить из файла',
                                  activebackground='grey', bg='#E5E5E5')
        self.upd_btn = tk.Button(self, text='Изменить данные',
                                 activebackground='grey', bg='#E5E5E5')
        self.del_btn = tk.Button(self, text='Удалить товар',
                                 activebackground='grey', bg='#E5E5E5')
        self.sup_btn = tk.Button(self, text='Поставка ',
                                 activebackground='grey', bg='#E5E5E5')
        self.sold_btn = tk.Button(self, text='Продажа',
                                  activebackground='grey', bg='#E5E5E5')
        self.max_pr_btn = tk.Button(self, text='Макс. цена',
                                    activebackground='grey', bg='#E5E5E5')
        self.min_pr_btn = tk.Button(self, text='Мин. цена',
                                    activebackground='grey', bg='#E5E5E5')
        self.name_s_btn = tk.Button(self, text='по имени',
                                    activebackground='grey', bg='#E5E5E5')
        self.price_s_btn = tk.Button(self, text='по цене',
                                     activebackground='grey', bg='#E5E5E5')
        self.count_s_btn = tk.Button(self, text='по количеству',
                                     activebackground='grey', bg='#E5E5E5')
        self.all_btn = tk.Button(self, text='Показать все товары',
                                 activebackground='grey', bg='#E5E5E5')
        self.get_btn = tk.Button(self, text='Ввод', activebackground='grey',
                                 state=tk.DISABLED)

        self.add_btn.grid(row=3, column=0, stick='we')
        self.find_btn.grid(row=2, column=0, stick='we')
        self.file_btn.grid(row=6, column=2, columnspan=2, stick='we')
        self.upd_btn.grid(row=4, column=0, stick='we')
        self.del_btn.grid(row=5, column=0, stick='we')
        self.sup_btn.grid(row=4, column=1, stick='we')
        self.sold_btn.grid(row=5, column=1, stick='we')
        self.max_pr_btn.grid(row=6, column=0, stick='we')
        self.min_pr_btn.grid(row=6, column=1, stick='we')
        self.name_s_btn.grid(row=1, column=1, stick='we')
        self.price_s_btn.grid(row=2, column=1, stick='we')
        self.count_s_btn.grid(row=3, column=1, stick='we')
        self.all_btn.grid(row=0, column=0, rowspan=2, stick='wens')
        self.get_btn.grid(row=4, column=2, rowspan=2,
                          columnspan=2, stick='wens')

        self.sort_lbl = tk.Label(self, text='Сортировка:',
                                 font=('@Microsoft JhengHei UI', 10))
        self.name_lbl = tk.Label(self, text='Наименование', state=tk.DISABLED,
                                 font=('@Microsoft JhengHei UI', 10))
        self.price_lbl = tk.Label(self, text='Цена', state=tk.DISABLED,
                                  font=('@Microsoft JhengHei UI', 10))
        self.count_lbl = tk.Label(self, text='Количество', state=tk.DISABLED,
                                  font=('@Microsoft JhengHei UI', 10))
        self.file_lbl = tk.Label(self, text='Файл', state=tk.DISABLED,
                                 font=('@Microsoft JhengHei UI', 10))
        self.name_goods_lbl = tk.Label(self, text='Наименование',
                                       font=('@Microsoft JhengHei UI', 10))
        self.price_goods_lbl = tk.Label(self, text='Цена',
                                        font=('@Microsoft JhengHei UI', 10))
        self.count_goods_lbl = tk.Label(self, text='Количество',
                                        font=('@Microsoft JhengHei UI', 10))

        self.sort_lbl.grid(row=0, column=1)
        self.name_lbl.grid(row=0, column=2)
        self.price_lbl.grid(row=1, column=2)
        self.count_lbl.grid(row=2, column=2)
        self.file_lbl.grid(row=3, column=2)
        self.name_goods_lbl.grid(row=7, column=0, columnspan=2)
        self.price_goods_lbl.grid(row=7, column=2)
        self.count_goods_lbl.grid(row=7, column=3)

        self.input_name = tk.Entry(self, state=tk.DISABLED)
        self.input_price = tk.Entry(self, state=tk.DISABLED)
        self.input_count = tk.Entry(self, state=tk.DISABLED)
        self.input_file = tk.Entry(self, state=tk.DISABLED)

        self.input_name.grid(row=0, column=3, stick='we')
        self.input_price.grid(row=1, column=3, stick='we')
        self.input_count.grid(row=2, column=3, stick='we')
        self.input_file.grid(row=3, column=3, stick='we')

        self.goods = scrolledtext.ScrolledText(self, width=40,
                                               height=30, state=tk.DISABLED,
                                               font=('Lucida Console', 11))
        self.goods.grid(row=8, column=0, columnspan=7, stick='wens')
