import json

numbers = "Sasha"

f = open('numbers.json', 'w')
json.dump(numbers, f)
f.close()