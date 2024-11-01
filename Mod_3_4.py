def same_root_words(root_word, *args):
    args_up_list = []
    same_words = []
    for i in range(len(args)):
#преобразуем в строки
        str_ = str(args[i])
#унифицируем регистр
        str_ = str_.lower()
#создаем список слов в нижнем регистре
        args_up_list.append(str_)
#проверяем наличие корня
        root_word = root_word.lower()
        if str_.count(root_word) != 0 or str_ in root_word:
#создаем список однокоренных слов в исходном виде
            same_words.append(args[i])
    print(same_words)



same_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')