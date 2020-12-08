n, k, m  = map(int,input().split())
a = list(map(int,input().split()))

ans = -1
if sum(a) + k >=  n*m:
    if n*m - sum(a) < 0:
        ans = 0
    else:
        ans = n*m - sum(a)
print(ans)