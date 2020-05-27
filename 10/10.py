import matplotlib.pyplot as plt
from simple_benchmark import benchmark


def loop(n):
    for i in range(2, 6):  # добавить m
        a.append(n ** i)
    return a


def tail(n):  # добавить m
    return tail_list(2, n)  # добавить m


def tail_list(iter, n):
    if iter > 6:
        return b
    b.append(n ** iter)
    return tail_list(iter + 1, n)


n = int(input("Введите число: "))
m = int(input("Введите максимальную степень: "))
a = []
b = []

defenitions = [loop, tail]

arguments = {}

for i in range(100):
    arguments['i' + str(i)] = i

argument_name = 'size of number'
aliases = {loop: 'Цикл', tail: 'Хвостовая рекурсия'}

c = benchmark(defenitions, arguments, argument_name, function_aliases=aliases)
c.plot()
plt.show(c)
