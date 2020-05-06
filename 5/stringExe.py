number = int(input())
stroka = str(number)
spisok = list(stroka)
# sorted_spisok = reversed(sorted(spisok)) - первый способ
# sorted_spisok = sorted(spisok, reverse=True) - второй способ
# spisok.sort()
# spisok.reverse()
spisok.sort()
spisok = spisok[::-1]
res_stroka = "".join(spisok)
res_number = int(res_stroka)
print(res_number)
