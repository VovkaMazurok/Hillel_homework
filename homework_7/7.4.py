def common_elements():
    numbers_multiples_3 = set()
    numbers_multiples_5 = set()

    for i in range(0, 100, 5):
        numbers_multiples_3.add(i)

    for i in range(0, 100, 3):
        numbers_multiples_5.add(i)

    intersection_set = numbers_multiples_3.intersection(numbers_multiples_5)

    return intersection_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')