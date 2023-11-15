from shops import *

if __name__ == '__main__':
    pizza = Pizza(2, 'Pizza 1', 15.99, ['cheese', 'pepperoni'], True, 12)
    coffee = Coffee(3, 'Coffee 1', 4.99, 16, 'latte')

    table = Table(5, 'Table 1', 99.99, 'glass', 'round')
    chair = Chair(6, 'Chair 1', 49.99, 'metal', True)
    cabinet = Cabinet(7, 'Cabinet 1', 149.99, 'plywood', 2)

    book = Book(9, 'Book 1', 12.99)
    magazine = Magazine(10, 'Magazine 1', 3.99)

    motherboard = Motherboard(12, 'Motherboard 1', 99.99)
    graphics_card = GraphicsCard(13, 'GraphicsCard 1', 199.99)
    storage = Storage(14, 'Storage 1', 79.99)

    # Создание экземпляров магазинов
    real_shop = RealShop()
    furniture_shop = ShopFurniture()
    books_shop = ShopBooks()
    computers_shop = ShopComputers()

    # Добавление продуктов в магазины
    real_shop.add_product(pizza)
    real_shop.add_product(coffee)

    furniture_shop.add_product(table)
    furniture_shop.add_product(chair)

    books_shop.add_product(book)
    books_shop.add_product(magazine)

    computers_shop.add_product(motherboard)
    computers_shop.add_product(graphics_card)
    computers_shop.add_product(storage)

print()
# ошибки при добавлении в магазин не того товара
try:
    furniture_shop.add_product(pizza)
except NonProductError:
    print('Вызываем ошибку в ShopFurniture')

try:
    books_shop.add_product(pizza)
except NonProductError:
    print('Вызываем ошибку в ShopBooks')

try:
    computers_shop.add_product(pizza)
except NonProductError:
    print('Вызываем ошибку в ShopComputers')
