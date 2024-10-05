def is_even(digit):
    """ Перевірка чи є парним число """
    check = lambda numb: True if digit % 2 == 0 else False
    return check(digit)

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
