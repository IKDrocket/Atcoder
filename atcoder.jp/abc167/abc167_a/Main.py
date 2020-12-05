s =input()
t = list(input())
del t[-1]

t= ''.join(t)
if s == t:
    print('Yes')
else:
    print('No')