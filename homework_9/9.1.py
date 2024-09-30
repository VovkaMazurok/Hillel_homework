def popular_words (text, words):

    """ Функція перевіряє чи знаходяться в тексті слова зі списку,
     та повертає результат ви вигляді словника де ключ це слово зі списку,
     значення це кількість повторень слова в тексті

     параметри: Текст і масив слів, що шукаються
     return: Словник, у якому ключами є шукані слова та значеннями,
      скільки разів кожнє слово зустрічаються у орігінальному тексті"""

    m_dict = dict()
    new_text = text.lower().split()
    for word in words:
        numb = new_text.count(word)
        m_dict[word] = numb
    return m_dict

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
