import string
Alp = list(string.ascii_uppercase)

s = input()
print('A') if s in Alp else print('a')