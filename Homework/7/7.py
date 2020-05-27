import os
import time


def diary(text):
    date = time.strftime("%d.%m.%Y", time.localtime())
    file_name = str((date) + '/' + time.strftime("%H.%M %d.%m.%Y", time.localtime()) + '.txt')
    os.mkdir(date)
    note = open(file_name, 'w', encoding='utf-8')
    note.write(text)
    note.close()


text = input("Введите текст Вашей заметки: ")
diary(text)