from codecs import namereplace_errors

print('Щоб вийти з калькулятора  введіть "yes"')
while True:
    text = input('Ви хочете вийти зькалькулятора? ')
    if text == 'yes':
        break
    else:
        x = int(input("Введіть перше число: "))
        w = input("Введіть математичну дію: ")
        y = int(input("Введіть друге число: "))

        if w == "+":
            print(x + y)
        elif w == "-":
            print(x - y)
        elif w == "*":
            print(x * y)
        elif w == "/":
            if y == 0:
                print("Дільник не може дорівнювати 0!")
                y = int(input("Введіть число яке не дорювнює 0: "))
        print(x / y)
