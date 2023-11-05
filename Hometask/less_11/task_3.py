# Необходимо создать класс KgToPounds, в который принимает количество
# килограмм, а с помощью метода to_pounds() они переводятся в фунты.
# Необходимо закрыть доступ к переменной kg.
# Также, реализовать методы:
# - set_kg() - для задания нового значения килограммов (записывать только
# числовые значения),
# - get_kg() - для вывода текущего значения кг.
# Во второй версии необходимо использовать декоратор property для создания
# setter и getter взамен set_kg и get_kg.

class KgToPounds_1:

    def __init__(self, kg: int | float):
        self.__kg = kg

    def to_pounds(self) -> int | float:
        return self.__kg * 2.20462

    def set_kg(self, new_kg: int | float) -> None:
        if type(new_kg) == int or type(new_kg) == float:
            self.__kg = new_kg
        else:
            print(f"Принят тип данных: {type(new_kg)}, должен быть int или float.")

    def get_kg(self) -> int | float:
        return self.__kg


class KgToPounds_2:

    def __init__(self, kg: int | float):
        self.__kg = kg

    def to_pounds(self) -> int | float:
        return self.__kg * 2.20462

    @property
    def kg(self) -> int | float:
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if type(new_kg) == int or type(new_kg) == float:
            # Оказывается тип данных bool наследуется от  типа int и при использовании функции
            # isinstance(new_kg, int) спокойно проходит проверку, и в целом работает, прикол.
            self.__kg = new_kg
        else:
            print(f"Принят тип данных: {type(new_kg)}, должен быть int или float.")


kg_to = KgToPounds_1(15)
kg_to.set_kg(15)
kg_to.set_kg('15')
print(kg_to.to_pounds())
print(kg_to.get_kg())
print()

kg_to = KgToPounds_2(15)
kg_to.kg = 15
kg_to.kg = '15'
print(kg_to.to_pounds())
print(kg_to.kg)
