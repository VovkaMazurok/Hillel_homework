lst = [12, 3, 4, 10] # [10, 12, 3, 4]
#lst = [1] # [1]
#lst = [] # []
#lst = [12, 3, 4, 10, 8] # [8, 12, 3, 4, 10]

# Перевіряємо чи список містить елементи і
# робим перестановку елементу з кінця списку на початок
if lst:
    x = lst.pop()
    lst.insert(0, x)
    print(lst)
else:
    print(lst)