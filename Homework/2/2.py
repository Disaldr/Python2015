import random
number = random.randint(1, 100)
level = int(input("Выбери уровень сложности\n1- Легко\n2-Нормально\n3-сложно\n"))
attempts = 3 * (5 - level)
player_number = 0
while attempts != 0:
    player_number = int(input("Введи число от 1 до 100: "))
    if player_number == number:
        print("Вы угадали!!!")
        break
    elif player_number < number:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    attempts -= 1
    print("Осталось "+str(attempts)+" попыток")
else:
    print("Вы не угадали! Загаданное число - "+str(number))