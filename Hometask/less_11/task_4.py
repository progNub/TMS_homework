# Строки в Питоне сравниваются на основании значений символов. Т.е. если мы
# захотим выяснить, что больше: Apple или Яблоко, – то Яблоко окажется
# бОльшим. А все потому, что английская буква A имеет значение 65 (берется из
# таблицы кодировки), а русская буква Я – 1071. Надо создать новый класс
# RealString, который будет принимать строку и сравнивать по количеству
# входящих в них символов. Сравнивать между собой можно как объекты класса,
# так и обычные строки с экземплярами класса RealString.

class RealString:

    def __init__(self, text: str):
        self.text = text

    def __str__(self) -> str:
        return self.text

    def __len__(self) -> int:
        return len(self.text)

    def __lt__(self, other) -> bool:
        """Определяет поведение оператора сравнения «меньше», <."""
        return len(self.text) < len(other)

    def __gt__(self, other) -> bool:
        """Определяет поведение оператора сравнения «больше», >."""
        return len(self.text) > len(other)

    def __le__(self, other) -> bool:
        """Определяет поведение оператора сравнения «меньше или равно», <=."""
        return len(self.text) <= len(other)

    def __ge__(self, other) -> bool:
        """Определяет поведение оператора сравнения «больше или равно», >=."""
        return len(self.text) >= len(other)

    def __eq__(self, other) -> bool:
        """Определяет поведение оператора «равенства», ==."""
        return len(self.text) == len(other)

    def __ne__(self, other) -> bool:
        """Определяет поведение оператора «неравенства», !=."""
        return len(self.text) != len(other)


t1 = RealString('012345')
t2 = RealString('0123456789')

print(f'{t1} > {t2} : {t1 > t2}')
print(f'{t1} < {t2} : {t1 < t2}')
print(f'{t1} != {t2} : {t1 != t2}')
print(f'{t1} == {t2} : {t1 == t2}')
print(f'{t1} >= {t2} : {t1 >= t2}')
print(f'{t1} <= {t2} : {t1 <= t2}')

tex = '12345678'
print()
print(f'{t1} > {tex} : {t1 > tex}')
print(f'{t1} < {tex} : {t1 < tex}')
print(f'{t1} != {tex} : {t1 != tex}')
print(f'{t1} == {tex} : {t1 == tex}')
print(f'{t1} >= {tex} : {t1 >= tex}')
print(f'{t1} <= {tex} : {t1 <= tex}')
