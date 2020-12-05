n, q = map(int,input().split())
a = []
for i in range(n):
    a.append(0)
L = []
R = []
T = []
for i in range(q):
    l,r,t = map(int,input().split())
    L.append(l)
    R.append(r)
    T.append(t)
for i in range(q):
    for j in range(L[i]-1,R[i]):
        a[j] = T[i]
for i in range(n):
    print(a[i])