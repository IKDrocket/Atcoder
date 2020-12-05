n,m = map(int,input().split(' '))
h = list(map(int,input().split(' ')))
ansList = [1]*n
numlist = []

for i in range(m):
    a,b = map(int, input().split())
    if h[a-1] > h[b-1]:
        #ansList[a-1] = ma
        numlist.append(b-1)
    elif h[a-1] == h[b-1]:
        numlist.append(a-1)
        numlist.append(b-1)
    else:
        numlist.append(a-1)
for i in list(set(numlist)):
    ansList[i] = 0
print(ansList.count(1))