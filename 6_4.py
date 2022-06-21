# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

from random import choice


class Car:
    direction = ["направо", "налево", "назад"]

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(F'Машина {name} {color} полицейская? {is_police}')

    def go(self):
        print(F"{self.name} поехала!")

    def show_speed(self):
        print(F"Скорость автомобиля {self.name} составляет {self.speed} км в час")

    def stop(self):
        print(F"{self.name} остановилась")

    def turn(self):
        print(F"Машина {self.name} повернула {choice(self.direction)}")


class TownCar(Car):
    def show_speed(self):
        n = float(self.speed)
        if n > 60:
            print(F"Превышение скорости {self.name}")
        else:
            print(F"Скоростной режим {self.name} не нарушен")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        n = float(self.speed)
        if n > 40:
            print(F"Превышение скорости {self.name}")
        else:
            print(F"Скоростной режим {self.name} не нарушен")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


townCar_1 = TownCar(80, 'red', 'Нива')
workCar_1 = WorkCar(35, 'blue', 'MAN')
sportCar_1 = SportCar(65, 'blue', 'Tayota')
policeCar_1 = PoliceCar(40, 'white', 'Lada')

car_car = [townCar_1, workCar_1, sportCar_1, policeCar_1]

for n in car_car:
    n.go()
    n.turn()
    n.show_speed()
    n.stop()
