def difference(*numb):

    """  Функція шукає різницю між найбільшим (максимум) і найменшим (мінімум) елементом.
         Якщо аргументів немає, то функція повертає 0 (нуль).

         параметри: Змінна кількість аргументів як числа (int, float)
         return: Різниця між максимумом і мінімумом як число (int, float)"""
    if numb:
        my_lst = list(numb)
        my_lst.sort()
        return  round(my_lst[-1] - my_lst[0], 2)
    else:
        return 0


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

