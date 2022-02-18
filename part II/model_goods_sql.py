from sqlalchemy import create_engine, Integer, String, Column, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


# подключение к серверу PostgreSQL
# username, password - данные для получения доступа к БД
# database - название БД
engine = create_engine(
        'postgresql+psycopg2://username:password@localhost/database'
)
Base = declarative_base()


class Goods(Base):

    """Класс Goods, описывающий товар в PostgreSQL"""

    __tablename__ = 'Goods'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    price = Column('price', Integer)
    count = Column('count', Integer)

    def __repr__(self):
        return f'{self.name.ljust(52)}' \
               f'{str(self.price).ljust(22)}' \
               f'{str(self.count).ljust(10)}'


connection = engine.connect()
Base.metadata.create_all(engine)


class GoodsMethods:

    """Класс GoodsMethods, описывающий
    методы взаимодействия с товарами"""

    @staticmethod
    def check_goods(value):
        """Проверка наличия товара в БД"""
        session = Session(bind=engine)
        if (value,) not in session.query(Goods.name).all():
            raise ValueError(f'Товара "{value}" нет в базе данных')

    @staticmethod
    def create_goods_from_file(name_file):
        """
        Добавляет товары в БД из файла

        :param name_file: имя файла
        :type name_file: str

        :return: список товаров в БД
        :rtype: list
        """
        with open(name_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            list_of_goods = []

            for goods in lines:
                dict_goods = dict()
                line_goods = goods.rstrip('\n').split(':')
                dict_goods['name'] = line_goods[0]
                dict_goods['price'] = line_goods[1]
                dict_goods['count'] = line_goods[2]

                list_of_goods.append(dict_goods)

        session = Session(bind=engine)

        for line in list_of_goods:
            goods = Goods(
                    name=line['name'],
                    price=line['price'],
                    count=line['count']
            )
            session.add(goods)

        session.commit()
        return session.query(Goods).all()

    @staticmethod
    def show_all():
        """
        Показать все товары в БД

        :return: список товаров в БД
        :rtype: list
        """
        session = Session(bind=engine)
        return session.query(Goods).all()

    @staticmethod
    def find_goods(name_goods):
        """
        Поиск товара по Наименованию

        :param name_goods: Наименование товара
        :type name_goods: str

        :return: список найденных товаров в БД
        :rtype: list
        """
        session = Session(bind=engine)

        if len(session.query(Goods).filter(
                Goods.name.ilike(f'%{name_goods}%')).all()) == 0:
            raise ValueError(f'Товара "{name_goods}" нет в базе данных')

        return session.query(Goods).filter(
                Goods.name.ilike(f'%{name_goods}%')).all()

    @staticmethod
    def add_goods(new_name, new_price, new_count):
        """
        Добавляет товар в БД

        :param new_name: Наименование нового товара
        :type new_name: str

        :param new_price: Цена нового товара
        :type new_price: str

        :param new_count: Количество нового товара
        :type new_count: str

        :return: новый товар
        :rtype: object of Class Goods
        """
        session = Session(bind=engine)

        if (new_name,) in session.query(Goods.name).all():
            raise ValueError(f'Товар "{new_name}" уже есть в базе данных')

        new_goods = Goods(
                name=new_name,
                price=int(new_price),
                count=int(new_count)
        )
        session.add(new_goods)
        session.commit()
        return session.query(Goods).filter(Goods.name == new_name).one()

    @staticmethod
    def delete_goods(delete_name):
        """
        Удаляет товар из БД по Наименованию

        :param delete_name: Наименование удаляемого товара
        :type delete_name: str

        :return: удаленный товар
        :rtype: object of Class Goods"""
        GoodsMethods.check_goods(delete_name)
        session = Session(bind=engine)

        del_goods = session.query(Goods).filter(
                Goods.name == (delete_name,)).one()
        session.delete(del_goods)
        session.commit()
        return del_goods

    @staticmethod
    def update_goods(name_goods, new_price, new_count):
        """
        Изменение Цены, Количества товара в БД

        :param name_goods: Наименование изменяемого товара
        :type name_goods: str

        :param new_price: новая Цена товара
        :type new_price: str

        :param new_count: новое Количество товара
        :type new_count: str

        :return: товар с измененными данными
        :rtype: object of Class Goods
        """
        GoodsMethods.check_goods(name_goods)
        session = Session(bind=engine)

        update_goods = session.query(Goods).filter(
                Goods.name == name_goods).first()

        if new_price:
            update_goods.price = int(new_price)
        if new_count:
            update_goods.count = int(new_count)

        session.commit()
        return session.query(Goods).filter(Goods.name == name_goods).one()

    @staticmethod
    def supply_goods(name_goods, new_count):
        """
        Поставка товара

        :param name_goods: Наименование поступившего товара
        :type name_goods: str

        :param new_count: поступившее Количество товара
        :type new_count: str

        :return: товар с измененными данными
        :rtype: object of Class Goods
        """
        GoodsMethods.check_goods(name_goods)
        session = Session(bind=engine)

        session.query(Goods).filter(
                Goods.name == name_goods).update(
                {'count': Goods.count + int(new_count)}
        )
        session.commit()
        return session.query(Goods).filter(Goods.name == name_goods).one()

    @staticmethod
    def sold_goods(name_goods, new_count):
        """
        Продажа товара

        :param name_goods: Наименование проданного товара
        :type name_goods: str

        :param new_count: проданное Количество товара
        :type new_count: str

        :return: товар с измененными данными
        :rtype: object of Class Goods
        """
        GoodsMethods.check_goods(name_goods)
        session = Session(bind=engine)

        sold_goods = session.query(Goods).filter(
                Goods.name == name_goods).one()

        if sold_goods.count >= int(new_count):
            sold_goods.count -= int(new_count)
        else:
            raise OverflowError(f'Недостаточно '
                                f'{int(new_count) - sold_goods.count} '
                                f'единиц товара "{name_goods}"')

        session.commit()
        return session.query(Goods).filter(Goods.name == name_goods).one()

    @staticmethod
    def max_price_goods():
        """
        Товары с максимальной ценой

        :return: список товаров с макс. ценой
        :rtype: list
        """
        session = Session(bind=engine)
        max_price = session.query(func.max(Goods.price)).first()
        return session.query(Goods).filter(Goods.price.in_(max_price)).all()

    @staticmethod
    def min_price_goods():
        """
        Товары с минимальной ценой

        :return: список товаров с мин. ценой
        :rtype: list
        """
        session = Session(bind=engine)
        min_price = session.query(func.min(Goods.price)).first()
        return session.query(Goods).filter(Goods.price.in_(min_price)).all()

    @staticmethod
    def sort_name_goods():
        """Сортировка товаров по Наименованию

        :return: список отсортированных товаров
        :rtype: list
        """
        session = Session(bind=engine)
        return session.query(Goods).order_by(Goods.name).all()

    @staticmethod
    def sort_price_goods():
        """
        Сортировка товаров по Цене

        :return: список отсортированных товаров
        :rtype: list
        """
        session = Session(bind=engine)
        return session.query(Goods).order_by(Goods.price).all()

    @staticmethod
    def sort_count_goods():
        """
        Сортировка товаров по Количеству

        :return: список отсортированных товаров
        :rtype: list
        """
        session = Session(bind=engine)
        return session.query(Goods).order_by(Goods.count).all()
