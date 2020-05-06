while True:
    first = input()
    if first == "q":
        break
    second = input()
    try:
        answer = int(first)/int(second)
    except ZeroDivisionError:
        print("На ноль делить нельзя, вы чего?")
    except ValueError:
        print("Вы ввели строку")
    else:
        print(answer)