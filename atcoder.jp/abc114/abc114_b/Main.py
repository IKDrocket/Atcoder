s = list(input())
n = 753
ans = 1000
for i in range(len(s)-2):
    num = int(s[i]+s[i+1]+s[i+2])
    if ans > abs(n-num):
        ans = abs(n-num)
print(ans)