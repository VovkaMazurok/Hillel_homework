number = int(input('Введіть будь яке число: '))

# Перетворюємо на рядок та вставляємо між кожним елементом знак множення '*',
# за допомогою функції "eval" обчислюємо рядок, поки добуток стане <=9
while number > 9:
    text = "*".join(str(number))
    number = eval(text)

print(number)