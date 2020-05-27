import random
red = [i for i in range(2, 37, 2)]
black = [j for j in range(1, 37, 2)]
print("Числа на красном:", end=' ')
print(*red)
print("Числа на черном:", end=' ')
print(*black)
numbers = red + black
numbers.append(0)
num = random.choice(numbers)
bet = input("Выберите ставку:\nК - красное\nЧ - чёрное\nили введите число на которое хотите поставить\n").upper()
if bet == "К":
    if num in red:
        print("Ставка сыграла")
    else:
        print("Вы проиграли")
elif bet == "Ч":
    if num in black:
        print("Ставка сыграла")
    else:
        print("Вы проиграли")
elif int(bet) == num:
    print("Ставка сыграла")
else:
    print("Вы проиграли")
print("Выпало "+str(num) + " " + (num in red)*"красное" + (num in black) * "чёрное" )