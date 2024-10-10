def is_even(number):
    """
            Перевіряє на парність число за допомогою побітової операції &
            Якщо число парне, результат буде 0, якщо ні то буде 1.
            В парних числа остання цифра бітового коду рівна 0, в непарних 1
            0 & 1 = 0
            1 & 1 = 1

            :param number: Ціле число для перевірки на парність.
            :return: Повертає True, якщо число парне, і False, якщо число непарне.
    """
    if (number & 1) == 0:
        return True
    else:
        return False

assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
