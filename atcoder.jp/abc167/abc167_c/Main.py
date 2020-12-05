n,m,x = map(int,input().split())
c = [0]*n
a = []
ans = float('inf')

for i in range(n):
    l = list(map(int,input().split()))
    c[i] = l.pop(0)
    a.append(l)

for bit in range(1<<n):
    s = [0]*m
    sumnum = 0
    for i in range(n):
        if 1 & (bit>>i):
            sumnum += c[i]
            for j in range(m):
                s[j] += a[i][j]
    flag = True
    for k in range(m):
        if s[k] < x:
            flag = False
            break
    if flag:
        ans = min(ans, sumnum)

if ans != float('inf'):
    print(ans)
else:
    print(-1)