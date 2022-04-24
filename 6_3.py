class Worker:
    name = "Иван"
    surname = "Иванов"
    position = "менеджер по работе с клиентами"
    __income = {"wage": 20000, "bonus": 5000}

    def set_income(self, wage, bonus):
        self.__income["wage"] = wage
        self.__income["bonus"] = bonus


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._Worker__income["wage"] + self._Worker__income["bonus"]


p = Position()
p.name = "Петр"
p.surname = "Петров"
print(p.get_full_name())
print(p.get_total_income())
p.set_income(30000, 10000)
print(p.get_total_income())
