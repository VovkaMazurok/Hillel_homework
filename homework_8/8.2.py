def is_palindrome(text):
    cleaned_text = ''
    # Проходимо по кожному символу в рядку
    for char in text:
        # Якщо символ є літерою або цифрою, додаємо його до результату
        if char.isalnum():
            cleaned_text += char.lower()
    # Порівнюємо очищений рядок з його перевернутою версією
    return cleaned_text == cleaned_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")