def generate_cube_numbers(end):
    """
        Генератор кубів чисел від 2 до тих пір, поки їх куби менші за дану величину.

        :param end: Межа для значень кубів чисел.
        :yield: Куб числа, меншу за end.

    """

    # Підносимо число до кубу
    def elevation_cube(x):
        return x ** 3

    for num in range(2, end):
        cube = elevation_cube(num)
        if cube > end:
            return
        yield cube

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'


