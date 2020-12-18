n, a, b = map(int,input().split())

ans = ''
if a == 0:
    ans = 0
else:
    x = n // (a+b)
    mod = min(n%(a+b), a)  
    ans = a*x + mod
print(ans)