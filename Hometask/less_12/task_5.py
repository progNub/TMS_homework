from task_1_2 import Product, Pizza
from task_3_4 import AbstractShop


# 5. Создать проверки типа передаваемого параметра для методов `add_product`
# и `sell_product`, на вход должны передаваться только продукты. Проверять
# тип необходимо через функцию `isinstance`. Если тип передаваемого
# значения не является, каким либо продуктом, то должна вызываться ошибка
# `NonProductError ` (создать новый класс ошибки).
class NonProductError(TypeError):
    pass


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


if __name__ == '__main__':
    shop = RealShop()
    pizza = Pizza(id=0, name='Margherita', price=30, fill=['cheese', 'tomato'], spicy=False, diameter=30)
    shop.add_product(pizza)
    # ============================ Ошибка==================================
    shop.add_product(12334)
