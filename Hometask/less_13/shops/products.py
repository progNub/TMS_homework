from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float


@dataclass
class Pizza(Product):
    fill: list
    spicy: bool
    diameter: int


@dataclass
class Coffee(Product):
    size: int
    type_coffee: str


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


@dataclass
class Publications(Product):
    pass


@dataclass
class Book(Publications):
    pass


@dataclass
class Magazine(Publications):
    pass


@dataclass
class ComputerComponents(Product):
    pass


@dataclass
class Motherboard(ComputerComponents):
    pass


@dataclass
class GraphicsCard(ComputerComponents):
    pass


@dataclass
class Storage(ComputerComponents):
    pass
