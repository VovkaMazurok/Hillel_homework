numb = int(input("Введіть пятизначне число: "))

# Отримуємо залишок від ділення (останню цифру числа)
first = numb % 10

#Отримуємо наступне число зменшене на одну цифру з кінця (ділимо число з заокругленням до меншого)
numb //= 10

second = numb % 10
numb //= 10

third = numb % 10
numb //= 10

fourth = numb % 10
numb //= 10

fifth = numb % 10

# Формуємо перевернуте число
reversed_number = first * 10000 + second * 1000 + third * 100 + fourth * 10 + fifth

print(reversed_number)