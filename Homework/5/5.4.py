import random
winner = random.randint(1,10)
results = ""
available = [i for i in range(1,10)]


def do_bet(horse, bet):
    global results
    if horse not in available or bet <= 0:
        results += 'Неверная ставка\n'
        return
    else:
        available.remove(horse)
        if horse == winner:
            results += f"Cтавка {bet} на лошадь {horse} была принята, вы выиграли {bet*2}\n"
        else:
            results += f"Cтавка {bet} на лошадь {horse} была принята, вы проиграли.\n"


inFlag = str(input('Хотите сделать ставку? Y/N: ').capitalize())
while inFlag == 'Y':
        horse = int(input('На какую лошадь вы ставите?: '))
        amount = int(input('Сколько вы ставите?: '))
        do_bet(horse, amount)
        inFlag = str(input('Хотите ещё сделать ставку? Y/N: ').capitalize())

print(f"Победила лошадь {winner}. Сводка по ставкам:\n", results)