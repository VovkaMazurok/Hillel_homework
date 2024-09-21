import string

text = input('Введіть дві літери англійського алфавіту через символ "-": ')

# Розділяємо літери по символу "-" і записуємо в окремі змінні
lst = text.split('-')
first = lst.pop(0)
second = lst.pop(-1)

# Визначаємо індекси введених літер в таблиці ascii
start_index = string.ascii_letters.index(first)
end_index = string.ascii_letters.index(second)

# Виводимо літери в межах вказаних літер по індексу
letters = string.ascii_letters[start_index:end_index+1]
print(letters)