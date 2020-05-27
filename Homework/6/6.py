numbers = open('input.txt')
numbersList = []
for i in numbers.readlines():
    numbersList.append(int(i))
print("Cумма =", sum(numbersList))
print("Среднее =", sum(numbersList)/len(numbersList))
numbers.close()