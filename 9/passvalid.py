import re

password = input()
result = re.match("(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,25}", password)
print(type(result))
if result:
    print(result.group(0))
else:
    print("Неправильный пароль")