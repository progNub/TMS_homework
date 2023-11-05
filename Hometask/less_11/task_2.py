# Требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого необходимо создать класс
# TriangleChecker, принимающий только положительные числа. С помощью
# метода is_triangle() возвращаются следующие значения (в зависимости от
# ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

class TriangleChecker:

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> None:
        a, b, c = self.a, self.b, self.c
        if not (all(isinstance(i, (int, float)) for i in (a, b, c))):
            print('Нужно вводить только числа!')
        elif min(a, b, c) < 0:
            print('С отрицательными числами ничего не выйдет!')
        elif a < b + c and b < a + c and c < a + b:
            print('Ура, можно построить треугольник!')
        else:
            print('Жаль, но из этого треугольник не сделать.')


triangle = TriangleChecker(10, 3, 8)
triangle.is_triangle()

triangle = TriangleChecker(-10, 3, 8)
triangle.is_triangle()

triangle = TriangleChecker('123', 3, 8)
triangle.is_triangle()

triangle = TriangleChecker(1, 3, 8)
triangle.is_triangle()
