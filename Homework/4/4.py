slovar = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'I',
    'Й': 'Y',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'u',
    'Ф': 'F',
    'Х': 'H',
    'Ц': 'Ts',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Щ': 'Sch',
    'Ъ': '',
    'Ы': 'Y',
    'Ь': '',
    'Э': 'E',
    'Ю': 'Y',
    'Я': 'Ya',
}

string = input('введите тест для транслитерации: ')
result = ""

for index, char in enumerate(string):
    symbol = char.upper()
    if symbol in slovar.keys():
        if char.isupper():
            result += slovar[symbol]
        else:
            result += slovar[symbol].lower()
    else:
        result += symbol

print(result)
