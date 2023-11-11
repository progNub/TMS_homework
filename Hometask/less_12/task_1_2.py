from dataclasses import dataclass


# 1. Создать dataclass `Product`, который содержит в себе поля id, name, price.
# Указать для полей типы int, str, float соответственно.

@dataclass
class Product:
    id: int
    name: str
    price: float


# 2. Создать dataclass `Pizza` и `Coffee`, которые наследуются от `Product ` и
# добавляют новые поля данных. Для пиццы это будет список начинки,
# острая или нет и диаметр. Для кофе будет объем стакана и его.

@dataclass
class Pizza(Product):
    fill: list
    spicy: bool
    diameter: int


@dataclass
class Coffee(Product):
    size: int
    type_coffee: str
