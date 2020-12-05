x, k = map(int,input().split())

r = x%k
ans = min(abs(r-k),r)
print(ans)