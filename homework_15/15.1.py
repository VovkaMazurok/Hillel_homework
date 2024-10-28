import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        new_square = self.get_square() + other.get_square()
        return self.determination_height_rectangle(new_square)

#Використовує math.isqrt для знаходження найбільшої можливої початкової ширини.
#Зменшуємо ширину в циклі, поки площа не ділиться без залишку на цю ширину для визначення нової висоти.

    def determination_height_rectangle(self, area):
        new_height = int(math.sqrt(area))
        while area % new_height != 0:
            new_height -= 1
        new_width = area // new_height
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        new_square = self.get_square() * n
        return self.determination_height_rectangle(new_square)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
