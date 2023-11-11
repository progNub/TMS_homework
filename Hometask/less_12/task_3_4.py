from abc import ABC, abstractmethod

from task_1_2 import Product, Pizza, Coffee


# 3. Создать абстрактный класс `AbstractShop`, который будет описывать
# абстрактные методы:
#  `add_product` — должен принимать тип `Product`
#  `sell_product` — должен принимать тип `Product`
#  `all_products` — должен возвращать список `Product`
# Данный абстрактный класс описывает требуемые методы для работы
# магазина (добавление нового товара, продажа и перечень всех).


class AbstractShop(ABC):

    @abstractmethod
    def add_product(self, product: Product):
        pass

    @abstractmethod
    def sell_product(self, product: Product):
        pass

    @abstractmethod
    def all_products(self):
        pass


# 4. Создать класс `RealShop`, который будет наследоваться от `AbstractShop` и
# реализовывать все его абстрактные методы.
# Данное заведение будет продавать пиццы и кофе.
# Проверить работоспособность каждого метода.


class RealShop(AbstractShop):

    def __init__(self):
        self._products = []

    def add_product(self, product: Product):
        self._products.append(product)
        print(f'{product.name}, товар был добавлен в список товаров, всего товаров: {len(self._products)}')

    def sell_product(self, product: Product):
        if product in self._products:
            self._products.remove(product)
            print(f"{product.name} - товар успешно продан, всего товаров: {len(self._products)}")
        else:
            print(f"{product.name} - такого товара не было найдено")

    def all_products(self):
        return self._products


if __name__ == '__main__':
    shop = RealShop()

    pizza = Pizza(id=0, name='Margherita', price=30, fill=['cheese', 'tomato'], spicy=False, diameter=30)
    shop.add_product(pizza)

    coffee = Coffee(id=1, name='Coffee 1', price=8, size=1, type_coffee='Latte')
    shop.add_product(coffee)

    print()
    print(shop.all_products())
    print()
    shop.sell_product(pizza)
    shop.sell_product(coffee)
    print()
    print(shop.all_products())
