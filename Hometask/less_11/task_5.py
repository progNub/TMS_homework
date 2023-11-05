# Напишите класс Rectangle, который имеет атрибуты width (ширина)
# и height (высота). Класс должен иметь следующие методы:
# • Конструктор, который принимает два параметра: width и height, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Rectangle в формате “Прямоугольник с шириной width и высотой height”.
# • Метод get_area, который возвращает площадь прямоугольника.
# • Метод get_perimeter, который возвращает периметр прямоугольника.
# • Метод is_square, который возвращает True, если прямоугольник является квадратом, и False в противном случае.
# Этот метод должен быть декорирован как property.

class Rectangle:

    def __init__(self, width: int | float, height: int | float):
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f'Прямоугольник с шириной: {self.width} и высотой: {self.height}'

    def get_area(self) -> int | float:
        return self.height * self.width

    def get_perimeter(self) -> int | float:
        return 2 * (self.height + self.width)

    @property
    def is_square(self) -> bool:
        return self.height == self.width
