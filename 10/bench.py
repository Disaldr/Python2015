from simple_benchmark import benchmark
from recursion import fact_rec
from hrecursion import fact_line
import matplotlib.pyplot as plt


def fact(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

funcs = [fact, fact_rec, fact_line]

arguments = {}
for i in range(1000):
    arguments['i'+str(i)] = i

argument_name = 'size of number'
aliases = {fact: 'Цикл', fact_rec: 'Простая рекурсия', fact_line: 'Хвостовая рекурсия'}

b = benchmark(funcs, arguments, argument_name, function_aliases=aliases)
b.plot()
plt.show(b)