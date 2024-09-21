def send_email(message , recipient , * , sender = "university.help@gmail.com"): # функция отправить письмо,
    # которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный
    # аргумент со значением по умолчанию sender = "university.help@gmail.com".

    if recipient == sender:  # если получатель и отправитель совпадают, то вывести запись
    # "Нельзя отправить письмо самому себе!"
        print("Нельзя отправить письмо самому себе!")

    # в первое условие функции нужно вывести сравнение получателя и отправителя, иначе при проверке условия
    # send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru') будет
    # выводится "Невозможно отправить письмо с адреса urban.teacher@mail.ru на адрес urban.student@mail.ru" вместо
    # нужного нам "Нельзя отправить письмо самому себе!"

    #if ("@" and (".com" or ".ru" or ".net")) not in recipient and ("@" and (".com" or ".ru" or ".net")) not in sender:
        # Если строки получатель и отправитель не содержит "@" и/или не оканчивается на ".com" или ".ru" или ".net"
        # , то вывести сообщение: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
        #print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)

    # "@" and (".com" or ".ru" or ".net") - условие, используемое для проверки получателя и отправителя.


    #elif recipient == sender: # если получатель и отправитель совпадают, то вывести запись
     #"Нельзя отправить письмо самому себе!"
    #   print("Нельзя отправить письмо самому себе!")

    elif "@" and (".com" or ".ru" or ".net") not in recipient and ("@" and (".com" or ".ru" or ".net")) not in sender:
        # Если строки получатель и отправитель не содержит "@" или не оканчивается на ".com" или ".ru" или ".net"
        # (любое из перечисленных), то вывести сообщение: "Невозможно отправить письмо с адреса <sender> на
        # адрес <recipient>".
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)


    elif sender == "university.help@gmail.com": # eсли же отправитель по умолчанию - university.help@gmail.com, то
    # вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)

    else: # В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender>
    # на адрес <recipient>."
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
