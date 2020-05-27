a = (1, -4, 6, 7, -10)

c = {"asd":1, "asdas":2, "sdasdsa":3 }

def func(x):
    if x == "asd":
        return 1
    else:
        return 0


b = filter(func, c)
b = dict(b)
print(b)