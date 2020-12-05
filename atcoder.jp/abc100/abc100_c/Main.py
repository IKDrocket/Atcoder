n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
    p = 0
    while i%2 == 0:
        i = i/2
        p += 1
    ans += p
print(ans)