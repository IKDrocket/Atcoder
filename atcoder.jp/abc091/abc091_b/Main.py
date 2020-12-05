N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]
S = list(set(s))
ans = 0
for i in S:
    ans = max(ans,s.count(i)-t.count(i))
print(ans)
