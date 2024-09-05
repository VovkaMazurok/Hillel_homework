numb = int(input("Введіть чотиризначне число: "))

# Отримуємо два числа: число від ділення із заокругленням до меншого, та залишок від ділення
left, right = divmod(numb,1000)
print(left)

left, right = divmod(right,100)
print(left)

left, right = divmod(right,10)
print(left)

print(right)