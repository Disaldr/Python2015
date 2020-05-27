import matplotlib.pyplot as plt
from simple_benchmark import benchmark


def loop(n):
    for i in range(1, 6):
        a.append(a[i-1]*n)
    return a


def tail(n):
    return tail_list(2, n)


def tail_list(iter, n):
    if iter > 6:
        return b
    b.append(n ** iter)
    return tail_list(iter + 1, n)


n = int(input("Введите число: "))
a = [1]
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
