from dataclasses import dataclass

from Hometask.less_12.task_1_2 import Product, Pizza
from Hometask.less_12.task_5 import RealShop


# 6. Создать магазин мебели, в котором будут продаваться столы, стулья и шкафы.
# Также необходимо создать на основе dataclass `Product` новый,
# общий для всех товаров в мебельном магазине, класс `Furniture`, каждый
# новый тип товара в этом магазине должен быть его предком.

# 7. Реализовать в методах `add_product` и `sell_product` проверку, что
# передаваемый продукт является мебелью через функцию `isinstance`. Если
# это не так, то необходимо вызвать ошибку `NonProductError `.

@dataclass
class Furniture(Product):
    material: str


@dataclass
class Table(Furniture):
    Table_top_shape: str


@dataclass
class Chair(Furniture):
    chair_back: bool


@dataclass
class Cabinet(Furniture):
    num_doors: int


class ShopFurniture(RealShop):

    def is_valid(self, product: Furniture, product_type=Furniture):
        super().is_valid(product, Furniture)


if __name__ == '__main__':
    table1 = Table(id=0, name='Table_1', price=250, material='wood', Table_top_shape='round')
    chair1 = Chair(id=1, name='Chair_1', price=100, material='metal', chair_back=True)
    cabinet1 = Cabinet(id=2, name='cabinet_1', price=300, material='wood', num_doors=4)

    pizza = Pizza(id=4, name='Margherita', price=30, fill=['cheese', 'tomato'], spicy=False, diameter=30)

    shop_furniture = ShopFurniture()

    shop_furniture.add_product(table1)
    shop_furniture.add_product(chair1)
    shop_furniture.add_product(cabinet1)

    shop_furniture.sell_product(table1)

    # ============================ Ошибка==================================
    shop_furniture.add_product(pizza)

    print(shop_furniture.all_products())
