import re


def valid_email(mail):
    if re.match(r'^\w*[\w\.\-]+\w*@\w+\.\w+$', mail):
        return True
    else:
        return False

def valid_login(login):
    if re.match(r'^[\w\.\-\@]+$', login):
        return True
    else:
        return False

# def valid_pass(password):
#     if re.match(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z$%#^]{8,}$', password):
#         return True
#     else:
#         return False

while True:
    email = input("Введите Вашу почту: ")
    login = input("Введите Ваш логин: ")
    if valid_email(email) and valid_login(login):
        users_list = open('users_list.txt', 'a', encoding='utf-8')
        users_list.write(email + ', ' + login + '\n')
        users_list.close()
        break
    elif not valid_email(email):
        print("Вы ввели не почту, введите данные заново")
    else:
        print("Вы ввели недопустимый логин, введите данные заново")