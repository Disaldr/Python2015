main_data = ['Egor', 'Petya', 'Vasya', 'Kesha']
name_length = map(len, main_data)
# name_length = []
# for i in range(len(main_data)):
#     name_length.append(len(main_data[i]))
print(list(name_length))

a, b = list(map(int, input().split()))
print(a * b)