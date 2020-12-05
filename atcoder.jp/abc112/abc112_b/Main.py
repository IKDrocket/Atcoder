n,T = map(int,input().split())
cc = 1001
tt = T + 1
for i in range(n):
    c,t = map(int,input().split())
    if t <= T and c <= cc:
        cc = c
        tt = t
if tt == T+1 or cc == 1001:
    print("TLE")
else:
    print(cc)