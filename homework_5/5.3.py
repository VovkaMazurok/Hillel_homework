import string

# Створюємо порожній рядок для зберігання символів без пунктуації,
# та початковий рядок хештега
hashtag = '#'
modified_string = ''

user_string = input('Enter your text: ')

# Якщо символ не є пунктуацією додаємо його до нового рядка
for char in user_string:
    if char not in string.punctuation:
        modified_string += char

# Розділяємо рядок на окремі слова та робимо першу літеру у верхньому регістрі
words_lst = modified_string.title().split()
for word in words_lst:
    hashtag += word

# Перевіряємо довжину хештега і скорочуємо його, якщо він більше 140 символів
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)