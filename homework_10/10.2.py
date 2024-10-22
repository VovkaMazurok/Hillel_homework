import string

def first_word(text):
    """ Пошук першого слова """
    # Видаляємо всі символи пунктуації та пробіли з початку рядка
    text = text.lstrip(string.punctuation + " ")

    word_chars = []  # Список для збирання символів першого слова

    # Перевіряємо чи символ є літера або дефіс/апостроф і додаємо до словника,
    # як тільки зустріли розділовий знак або пробіл — зупиняємось
    for char in text:
        if char.isalpha() or char in "-'":
            word_chars.append(char)
        else:
            break

    # Об'єднуємо список символів у рядок і повертаємо перше слово
    return ''.join(word_chars)

# Простіше рішення
#def first_word(text):
    #text = text.replace('.', ' ').replace(',', ' ').split()
    #return text[0]

# Тести
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')