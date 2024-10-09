lst_numb = [0, 2, 4, 6, 8]

def is_even(number):
    """
            Перевіряє на парність число

            :param number: Ціле число для перевірки на парність.
            :return: Повертає True, якщо число парне, і False, якщо число непарне.
    """
    last = int(str(number)[-1])

    if last in lst_numb:
        return True
    else:
        return False


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
