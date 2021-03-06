def create_file_of_goods(goods, name_file):
    """
    Создает файл с товарами из списка товаров

    :param goods: список товаров
    :type goods: list

    :param name_file: имя создаваемого файла
    :type name_file: str
    """
    if not isinstance(goods, list):
        raise ValueError('Список товаров должен быть типа list')

    if not isinstance(name_file, str) or len(name_file) == 0:
        raise ValueError('Имя файла должно быть непустой строкой')

    with open(name_file, 'w', encoding='utf-8') as new_file:
        for line in goods:
            new_file.write(line)


list_goods = [
    'молоко Хорская Буренка:70:5\n', 'молоко Фермерское:55:10\n',
    'молоко Простоквашино:66:5\n', 'хлеб серый хлебозавод:30:20\n',
    'яйцо 1 кат.:30:40\n', 'яйцо 2 кат.:30:40\n', 'яйцо 3 кат.:30:40\n',
    'макароны Макфа,рожки:30:10\n', 'макароны Макфа,спагетти:30:10\n',
    'сахар 1кг:40:30\n', 'соль 1 кг:35:30\n', 'масло сливочное:100:20\n',
    'масло подсолнечное:100:20\n', 'говядина 1кг:250:10\n',
    'свинина 1кг:220:10\n', 'баранина 1кг:210:10\n',
    'филе куринное 1кг:200:10\n', 'грудка куринная 1кг:225:10\n',
    'голень куринная 1кг:230:10\n', 'крылышки куринные 1кг:180:10\n',
    'рыба мороженая, Кета 1кг:400:5\n', 'рыба мороженая, Треска 1кг:300:5\n',
    'рыба мороженая, Горбуша 1кг:300:5\n', 'рыба мороженая, Окунь 1кг:300:5\n',
    'чай черный Greenfield 10 пак.:50:20\n',
    'Чай черный Lipton 10 пак.:60:20\n',
    'чай зеленый Greenfield 10 пак.:50:20\n',
    'Чай зеленый Lipton 10 пак.:60:20\n',
    'мука пшеничная Весёлый мельник 1кг.:40:20\n',
    'мука пшеничная Весёлый мельник 2кг.:60:10\n',
    'хлеб ржаной хлебозавод:50:20\n', 'сушки 1кг.:45:20\n',
    'пряники 1кг.:55:20\n', 'булочки плюшки:30:10\n',
    'пирожки с брусникой:30:10\n', 'пирожки с картошкой:30:2\n',
    'пирожки с вишней:30:10\n', 'рис шлифованный 1кг:40:10\n',
    'рис круглозерный 1кг:45:10\n', 'пшено 1кг:50:30\n',
    'крупа гречневая 1кг:60:30\n', 'вермишель Макфа 1кг:45:20\n',
    'картофель 1кг:60:50\n', 'капуста белокочанная 1кг:60:50\n',
    'лук репчатый 1кг:40:50\n', 'морковь 1кг:55:50\n',
    'яблоки Новая Зеландия 1кг:60:120'
]

file = '../part II/goods.txt'
create_file_of_goods(list_goods, file)
