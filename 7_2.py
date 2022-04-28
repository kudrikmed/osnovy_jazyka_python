from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def textile(self):
        pass

    def __add__(self, other):
        return self.textile + other.textile


class Coat(Clothes):
    def __init__(self, size):
        self.type = "coat"
        self.size = size

    @property
    def textile(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.type = "coat"
        self.height = height

    @property
    def textile(self):
        return 2 * self.height + 0.3


my_coat = Coat(4)
my_suit = Suit(6)

print(my_coat.textile)
print(my_suit.textile)
print(my_coat + my_suit)
