class Auto:

    def __init__(self, brand: str, age: int, mark: str, color: str = '', weight: int = 0):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1

# auto = Auto('Audi', 12, 'A8')
# auto.move()
