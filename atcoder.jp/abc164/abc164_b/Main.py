import math

a,b,c,d = map(int, input().split())
turn1 = math.ceil(c/b)
turn2 = math.ceil(a/d)
if turn1 <= turn2:
    print('Yes')
else:
    print('No')