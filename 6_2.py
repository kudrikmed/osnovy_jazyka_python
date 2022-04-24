from math import ceil


class Road:
    mass_for_one_sq_mr = 25
    thickness = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_mass(self):
        return ceil(self.__length * self.__width * self.mass_for_one_sq_mr * self.thickness / 1000)


r = Road(1000, 10)
print(f'Для покрытия дорожного полотна потребуется {r.get_mass()} т. асфальта')
