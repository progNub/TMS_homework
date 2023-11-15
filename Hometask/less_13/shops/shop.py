from .abstracts import AbstractShop
from .products import Product, Furniture, ComputerComponents, Publications
from .my_exeption import NonProductError


class RealShop(AbstractShop):

    def __init__(self):
        self._products = []

    def is_valid(self, product: Product, product_type=Product) -> None:
        """
        Этот метод является проверкой типа передаваемых дынных,
         сам тип данных, по которому идет проверка - является параметром метода
         это нужно для переопределения этого метода от будущих наследников

        :param product: Экземпляр какого-то товара.
        :param product_type: Тип класса по которому нужно делать проверку.
        """
        if not (isinstance(product, product_type)):
            raise NonProductError(f'"{product}" - не является экземпляром класса "{product_type}"')

    def add_product(self, product: Product) -> None:
        self.is_valid(product)
        self._products.append(product)
        print(f'{product.name}, товар был добавлен в список товаров, всего товаров: {len(self._products)}')

    def sell_product(self, product: Product) -> None:
        self.is_valid(product)
        if product in self._products:
            self._products.remove(product)
            print(f"{product.name} - товар успешно продан, всего товаров: {len(self._products)}")
        else:
            print(f"{product.name} - такого товара не было найдено")

    def all_products(self) -> list[str]:
        return self._products


class ShopFurniture(RealShop):

    def is_valid(self, product: Furniture, product_type=Furniture):
        super().is_valid(product, product_type)


class ShopBooks(RealShop):
    def is_valid(self, product: Publications, product_type=Publications):
        super().is_valid(product, product_type)


class ShopComputers(RealShop):
    def is_valid(self, product: ComputerComponents, product_type=ComputerComponents):
        super().is_valid(product, product_type)
