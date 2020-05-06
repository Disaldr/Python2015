import random

print("Приветствую в игре Транслатион! "
      "Введите слова и их переводы, а я "
      "проведу тестирование по этим словам!")

dictionary = {}

# Цикл для заполнения словаря
while True:
    key = input("Введите слово на английском или stop: ").title().strip()
    if key == "Stop":
        break
    value = input("Введите его перевод или stop: ").title().strip()
    if value == "Stop":
        break
    dictionary[key] = value


print("")

scores = 0
error = 0
flag = True
while flag:
    dictionary = list(dictionary.items())
    random.shuffle(dictionary)
    dictionary = dict(dictionary)

    for key, value in dictionary.items():
        translation = input("Введи перевод слова " + key + ": ").title().strip()
        if translation == value:
            scores += 1
        else:
            error += 1
        if error == 3:
            exit("Проиграл")
    flag = input("Введи True, если хочешь сыграть ещё раз")
print(scores)

"""
Подсчёт ошибок+
+Дружелюбие
Перемешать элементы словаря random.shuffle()
Проигрыш при условии 3 ошибок+
Перевести все вводные строки к нижнему регистру
Удалить пробелы в вводных строках
"""