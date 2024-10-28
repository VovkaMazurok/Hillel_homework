class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def reduction_common_denominator(self, other):

        # Визначаємо спільний знаменник
        lcm = self.b * other.b

        # Приводимо дроби до спільного знаменника
        new_self_a = self.a * (lcm // self.b)
        new_other_a = other.a * (lcm // other.b)
        return new_self_a, new_other_a, lcm

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        new_self_a, new_other_a, lcm = self.reduction_common_denominator(other)
        return Fraction(new_self_a + new_other_a, lcm)

    def __sub__(self, other):
        new_self_a, new_other_a, lcm = self.reduction_common_denominator(other)
        return Fraction(new_self_a - new_other_a, lcm)

    def __eq__(self, other):
        new_self_a, new_other_a, _ = self.reduction_common_denominator(other)
        return new_self_a == new_other_a

    def __gt__(self, other):
        new_self_a, new_other_a, _ = self.reduction_common_denominator(other)
        return new_self_a > new_other_a

    def __lt__(self, other):
        new_self_a, new_other_a, _ = self.reduction_common_denominator(other)
        return new_self_a < new_other_a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')