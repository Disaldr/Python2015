import re

text = input()
# Проверка на почту
result = re.match(r'^[a-zA-Z0-9_\.\-]+@\w+\.\w+$', text)
if result:
    print(result.group(0))
else:
    print("Вы ввели не почту")
# Проверка на телефон
# +7 123 1231234
result = re.match(r'(\+7|8|7)( |)\d{3}( |)\d{7}', text)
if result:
    print(result.group(0))
else:
    print("Вы ввели не телефон")