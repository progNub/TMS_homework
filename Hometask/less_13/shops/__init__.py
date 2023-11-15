from .products import Product, Pizza, Coffee, Furniture, Chair, Table, Cabinet, ComputerComponents, Publications, \
    Storage, GraphicsCard, Magazine, Motherboard, Book
from .shop import RealShop, ShopFurniture, ShopComputers, ShopBooks
from .abstracts import AbstractShop
from .my_exeption import NonProductError

# 1. Создать пакет shops, на основе классов из предыдущего задания. В пакете
# требуется организовать структуру из нескольких файлов.

# 2. Расширить перечень магазинов в пакете shops, добавив классы для книжного
# магазина и компьютерной техники.

# 3. Книжный магазин должен продавать только книги или журналы.

# 4. Магазин компьютерной техники должен продавать только комплектующие
# для компьютеров (материнские платы, видеокарты и пр.)

# 5. Из пакета shops должны импортироваться все классы магазинов без
# префиксов.

# Пример: from shops import RealShop

# shops:
#     __init__.py
#     abstracts.py
#     products.py
#     shop.py
# main.py
