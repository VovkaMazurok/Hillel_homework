number = int(input('Введіть будь яке число: '))

# Вираховуємо кількість секунд
a, seconds = divmod(number, 60)

# Вираховуємо кількість хвилин
b, minutes = divmod(a, 60)

# Вираховуємо кількість годин, залишок це кількість днів
days, hours = (divmod(b, 24))

# Визначаємо останню цифру числа
last_digit = days % 10

# Якщо остання цифра 1, але не дорівнює 11, використовуємо форму "день"
if last_digit == 1 and days != 11:
    result = f"{days} день"

    # Якщо остання цифра 2, 3 або 4, але менша за 11 та більша за 19, використовуємо форму "дні"
elif 2 <= last_digit <= 4 and 11 > days < 19:
    result = f"{days} дні"

    # У всіх інших випадках використовуємо форму "днів"
else:
    result = f"{days} днів"

# Виводимо результат
time_string = (result + ', ' + str(hours).zfill(2) + ':'
               + str(minutes).zfill(2) + ':' + str(seconds).zfill(2))
print(time_string)