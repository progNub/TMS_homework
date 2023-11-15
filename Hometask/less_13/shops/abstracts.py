from abc import ABC, abstractmethod

from .products import Product


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
