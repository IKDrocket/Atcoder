n = int(input())
w = list(map(int,input().split()))
ans = 1000
Ans = 1000
for i in range(1,n+1):
    front = []
    back = []
    front = w[:i]
    back = w[i:]
    diff = abs(sum(front) - sum(back))
    if diff < ans:
        ans = diff
        Ans = i
print(ans)