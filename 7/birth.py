day = int(input("Day of birth: "))

try:
    if day > 31 or day < 1:
        raise ValueError("Неправильная дата")
except ValueError:
    print("Ошибка!")
else:
    print(day)
finally:
    print("Jnkbxysq ctujlyz lty`r")