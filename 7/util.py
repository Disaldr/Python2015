import os
import shutil

while True:
    choice = input("Что делать? \nСоздавать - C\nУдалять - D\nВыход - Q\n").upper()
    if choice == "Q":
        exit()
    elif choice == "C":
        dir_name = input("Введите название создаваемой директории: ")
        os.mkdir(dir_name)
    elif choice == "D":
        dir_name = input("Введите название удаляемой директории: ")
        shutil.rmtree(dir_name)
