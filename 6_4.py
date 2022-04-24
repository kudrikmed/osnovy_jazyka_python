from random import randint, choice


class Car:
    def __init__(self, name, is_police):
        self.name = name
        self.is_police = is_police
        self.speed = randint(10, 200)
        self.color = choice(["red", "green", "white", "black", "yellow", "silver"])

    def go(self):
        print(f"{self.color.capitalize()} {self.name} is moving with speed {self.speed}")

    def stop(self):
        print(f"{self.color.capitalize()} {self.name} is stopped")

    def turn(self, direction):
        print(f"{self.color.capitalize()} {self.name} is turning {direction}")

    def show_speed(self):
        print(f"Current speed is {self.speed} k/h")


class TownCar(Car):
    def __init__(self):
        self.name = "TownCar"
        self.is_police = False
        self.speed = randint(40, 70)
        self.color = choice(["red", "green", "white", "black", "yellow", "silver"])

    def show_speed(self):
        if self.speed > 60:
            print(f"\033[31mAttention! High speed!\033[0m\n{self.color.capitalize()} {self.name} is moving with speed {self.speed}!")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self):
        self.name = "SportCar"
        self.is_police = False
        self.speed = randint(90, 150)
        self.color = choice(["red", "yellow", "silver"])


class WorkCar(Car):
    def __init__(self):
        self.name = "WorkCar"
        self.is_police = False
        self.speed = randint(20, 50)
        self.color = choice(["white", "black"])

    def show_speed(self):
        if self.speed > 40:
            print(f"\033[31mAttention! High speed!\033[0m\n{self.color.capitalize()} {self.name} is moving with speed {self.speed}!")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self):
        self.name = "PoliceCar"
        self.is_police = True
        self.color = "blue"
        self.speed = 90


TownCar = TownCar()
TownCar.go()
TownCar.show_speed()
WorkCarA = WorkCar()
WorkCarA.go()
WorkCarB = WorkCar()
WorkCarB.go()
WorkCarB.turn("left")
SportCarA = SportCar()
SportCarA.go()
SportCarB = SportCar()
SportCarB.go()
PoliceCar = PoliceCar()
print(PoliceCar.is_police)
