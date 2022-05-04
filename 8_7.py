class ComplexNumber:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return str((self.real, self.image))

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.image * other.image, self.real * other.image + other.real * self.image)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.image + other.image)


a = ComplexNumber(2, 3)
b = ComplexNumber(3, 1)
c = ComplexNumber(2, -3)

print(a + b)
print(b * c)
