import string
import keyword

# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

variable_name = input("Введіть ім'я змінної: ")

# Початково припускаємо, що ім'я валідне
valid = True

# Перевірка, що рядок не починається з цифри
if variable_name[0].isdigit():
    valid = False

# Перевірка, що рядок не містить великих літер
for char in variable_name:
    if char.isupper():
        valid = False
        break

# Перевірка, чи рядок не містить знаки пунктуації та пробіли,
# крім нижнього підкреслення "_"
for char in variable_name:
    if (char in string.punctuation and char != "_") or char.isspace():
        valid = False
        break

# Перевірка, що рядок не містить більше одного підкреслення поспіль або складається лише з підкреслень
if variable_name.count('_') > 1 and variable_name.replace('_', '') == '':
    valid = False

# Перевіряємо, чи є це слово зарезервованим словом
if variable_name in keyword.kwlist:
    valid = False

# Виведення результату
if valid:
    print(True)
else:
    print(False)
