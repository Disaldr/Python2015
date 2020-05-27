import os
import time

while True:
    answer = input("Хотите добавить заметку?\n")
    if answer != "Q":
        date = input("Введите дату:")
        text = input("Введите текст Вашей заметки: ")
        file_name = str((date) + '/' + time.strftime("%H.%M %d.%m.%Y", time.localtime()) + '.txt')
        try:
            os.mkdir(date)
        except:
            pass
        note = open(file_name, 'w', encoding='utf-8')
        note.write(text)
        note.close()
    else:
        exit(0)