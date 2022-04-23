class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} Машина поехала ')

    def stop(self):
        print(f"{self.name} Машина остановилась ")

    def turn(self):
        print(f"{self.name} Машина повернула {input('Введите направление ')} ")

    def show_speed(self):
        return f"Машина {self.name} скорость = {self.speed}"


class TownCar(Car):

    def show_speed(self):
        return f"{self.name} едет со скоростью {self.speed}" if self.speed > 60 else super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        return f"{self.name} едет со скоростью {self.speed}" if self.speed > 40 else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


police_car = PoliceCar(60, "Черная", "Полицейская")
police_car.go()
police_car.stop()
police_car.turn()
work_car = WorkCar(70, "Белая", "Рабочая")
work_car.go()
print(work_car.show_speed())
work_car.turn()
print(f"Машина полицеская" if work_car.is_police is True else "Машина не полцейская")
sports_car = SportCar(100, "Белая", "Спортивная")
sports_car.go()
print(work_car.show_speed())
sports_car.stop()
sports_car.turn()
print(f"Машина полицеская" if sports_car.is_police is True else "Машина не полцейская")
towncar = TownCar(80, "Белая", "Городская")
towncar.go()
print(work_car.show_speed())
towncar.stop()
towncar.turn()
print(f"Машина полицеская" if towncar.is_police is True else "Машина не полцейская")
