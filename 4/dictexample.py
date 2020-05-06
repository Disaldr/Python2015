family = {"dad": 60, "mother": 55, "aunt": 50, 'dad':40}
# print(family['dad'])
# family['uncle'] = 51
# print(*family)
new_dict = {"b":4, "a":5}

for a, b in family.items():
    print("Ключ - "+a+", значение - " + str(b))

print(*list(family.keys()))
print(*list(family.values()))


if 'dad' in family.keys():
    print('dad')
if 50 in family.values():
    print('50')

