import time

from task_1 import Auto


class Truck(Auto):

    def __init__(self, brand: str, age: int, mark: str, max_load, color: str = '', weight: int = 0):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('"attention"')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):

    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color: str = '', weight: int = 0):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        print(f'max_speed is {self.max_speed}')


truck_1 = Truck('Truck_1', 15, 'Truck_mark_1', 5000, 'Black', 6000)
truck_2 = Truck('Truck_2', 10, 'Truck_mark_2', 6000, 'yellow', 6000)
car_1 = Car('Car_1', 5, 'Car_mark_1', 240, 'Black', 1340)
car_2 = Car('Car_2', 2, 'Car_mark_2', 260, 'Red', 1250)

print(truck_1.brand, truck_1.age, truck_1.mark, truck_1.max_load, truck_1.color, truck_1.weight)
truck_1.load()
truck_1.birthday()
truck_1.move()
truck_1.stop()
print(truck_1.brand, truck_1.age, truck_1.mark, truck_1.max_load, truck_1.color, truck_1.weight)
print()

print(truck_2.brand, truck_2.age, truck_2.mark, truck_2.max_load, truck_2.color, truck_2.weight)
truck_2.load()
truck_2.birthday()
truck_2.move()
truck_2.stop()
print(truck_2.brand, truck_2.age, truck_2.mark, truck_2.max_load, truck_2.color, truck_2.weight)
print()

print(car_1.brand, car_1.age, car_1.mark, car_1.max_speed, car_1.color, car_1.weight)
car_1.move()
car_1.birthday()
car_1.stop()
print(car_1.brand, car_1.age, car_1.mark, car_1.max_speed, car_1.color, car_1.weight)
print()

print(car_2.brand, car_2.age, car_2.mark, car_2.max_speed, car_2.color, car_2.weight)
car_2.move()
car_2.birthday()
car_2.stop()
print(car_2.brand, car_2.age, car_2.mark, car_2.max_speed, car_2.color, car_2.weight)