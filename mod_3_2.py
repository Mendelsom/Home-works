def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if '@' not in recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif "@" not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif ".com" not in sender and '.ru' not in sender and '.net' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif ".com" not in recipient and '.ru' not in recipient and '.net' not in recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', sender='yuri.babkin@mail.ru')