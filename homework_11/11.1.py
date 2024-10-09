import math

def prime_generator(end):
    """
       Створює генератор простих чисел від 2 до end включно.

       :param end: Верхня межа для генерації простих чисел (включно).
       :yield: Просте число від 2 до end.

       """

    # Перевірка чи є число простим
    def is_prime(n):
        limit = int(math.sqrt(n))
        i = 2
        while i <= limit:
            if n % i == 0:
                return False
            i += 1
        return True

    # Якщо число просте, повертаємо його за допомогою yield
    for num in range(2, end + 1):

        if is_prime(num):
            yield num

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')