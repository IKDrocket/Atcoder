s = input()

n = len(s)
sf = s[:int((n-1)/2)]
sb = s[int((n+3)/2)-1:]

if s[::-1] == s and sf[::-1] == sf and sb[::-1] == sb:
    print('Yes')
else:
    print('No')