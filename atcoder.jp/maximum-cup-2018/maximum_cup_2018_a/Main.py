n=int(input())
ans = 0
for i in range(n):
    t,d,m = map(int,input().split())
    if t+10 <= d:
        ans += m
print(ans)
    