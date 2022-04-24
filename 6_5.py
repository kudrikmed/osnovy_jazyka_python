class Stationery:
    title = "Stationery"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print(f"\033[3m\033[34m{self.title}\033[0m")


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print(f"\033[37m\033[2m{self.title}\033[0m")


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print(f"\033[41m{self.title}\033[0m")


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
