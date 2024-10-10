import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    """
       Видаляє всі HTML-теги з вхідного файлу і записує очищений текст у вихідний файл.

       Параметри:
       html_file (str): Шлях до HTML-файлу, який потрібно очистити.
       result_file (str): Шлях до файлу, куди буде записано очищений текст. За замовчуванням 'cleaned.txt'.
    """

    # Відкриваємо вхідний HTML-файл для читання
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = ""

    #Позначка, яка вказує що ми всередині HTML - тегу
    inside_tag = False

    # Перебираємо кожен символ у вмісті файлу
    for char in html:
        if char == '<':
            # Встановлюємо позначку True, коли зустрічаємо відкриваючий тег
            inside_tag = True
        elif char == '>':
            # Встановлюємо позначку False, коли зустрічаємо закриваючий тег
            inside_tag = False
        elif not inside_tag:
            # Додаємо символ до очищеного тексту, якщо він не належить до тегу
            cleaned_text += char

    # Записуємо очищений текст у файл
    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_text)


delete_html_tags('draft.html')