def palindrome(string):
    temp = string.replace(' ', '')
    return temp.lower() == temp[::-1].lower()


print(palindrome(input()))