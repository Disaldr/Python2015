translated_text = ""


def translate(text):
    # Используем global чтобы ПРИСВОИТЬ значение, просто обратиться к ней мы могли бы и не используя global
    global translated_text
    translated_text = "".join(str(i) for i in text if i not in 'уеыаоэяию')


a = input()
translate(a)
print(translated_text)