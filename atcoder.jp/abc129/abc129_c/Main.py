n,m = map(int,input().split())
a = []
if m == 0:
    a = set()
else:
    for i in range(m):
        a.append(int(input()))
a = set(a)
dp = [0]*(n+1)
dp[0] = 1
if 1 in a:
    dp[1] = 0
else:
    dp[1] = 1
MOD = 10 ** 9 + 7

for i in range(2,n+1):
    if i in a:
        continue
    dp[i] = (dp[i-2] + dp[i-1]) % MOD
print(dp[n])