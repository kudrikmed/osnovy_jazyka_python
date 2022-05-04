from abc import abstractmethod, ABC


class NotEnoughTechnic(Exception):
    pass


class NotInt(Exception):
    pass


class NoSuchKindOfTechnique(Exception):
    pass


class Store:
    total = {"printer": 0, "scanner": 0, "copier": 0}
    delivery_note = {"accounting": {"printer": 0, "scanner": 0, "copier": 0},
                     "sales department": {"printer": 0, "scanner": 0, "copier": 0}}

    @staticmethod
    def add_technique(technique):
        Store.total[technique] += 1

    @staticmethod
    def check_int(value):
        try:
            if isinstance(value, int) and value > 0:
                return True
            else:
                raise NotInt
                return False
        except NotInt:
            print("Number of technique must be positive int value!")

    @staticmethod
    def receive_technique(technique, number):
        if Store().check_int(number):
            try:
                if technique == "printer":
                    for tech in range(number):
                        tech = Printer()
                elif technique == "scanner":
                    for tech in range(number):
                        tech = Scanner()
                elif technique == "copier":
                    for tech in range(number):
                        tech = Copier()
                else:
                    raise NoSuchKindOfTechnique
            except NoSuchKindOfTechnique:
                print("There is no such kind of technique at store")

    @staticmethod
    def send_technique(cls, department):
        try:
            if Store.total[cls.technique_type] > 0:
                Store.total[cls.technique_type] -= 1
                Store.delivery_note[department][cls.technique_type] += 1
            else:
                raise NotEnoughTechnic
        except NotEnoughTechnic:
            print(f"Not enough {cls.technique_type}s at store")


class Technique(ABC):
    @abstractmethod
    def consume_energy(self):
        pass

    def move_to(self, department):
        Store.total[self.technique_type] -= 1
        Store.delivery_note[department][self.technique_type] += 1

    def __init__(self):
        self.technique_type = "technique"


class Printer(Technique):
    def __init__(self):
        self.technique_type = "printer"
        Store.add_technique(self.technique_type)

    def consume_energy(self):
        print("Consuming 4 energy...")

    def start_printing(self):
        print("Printing in progress...")


class Scanner(Technique):
    def __init__(self):
        self.technique_type = "scanner"
        Store.add_technique(self.technique_type)

    def consume_energy(self):
        print("Consuming 2 energy...")

    def start_scanning(self):
        print("Scanning in progress...")


class Copier(Technique):
    def __init__(self):
        self.technique_type = "copier"
        Store.add_technique(self.technique_type)

    def consume_energy(self):
        print("Consuming 5 energy...")

    def start_copying(self):
        print("Copying in progress...")


p1 = Printer()
p1.start_printing()
p2 = Printer()
s1 = Scanner()
print(Store().total)
print(p1.technique_type)
Store.send_technique(p1, "accounting")
Store.send_technique(p2, "accounting")
Store.send_technique(p2, "accounting")
print(Store().total)
print(Store().delivery_note)
s1.move_to("sales department")
print(Store().total)
print(Store().delivery_note)
Store.receive_technique("printer", 5)
Store.receive_technique("copier", "2")
print(Store.total)
