n,k = map(int,input().split())
s = list(input())
s[k-1] = s[k-1].lower()
ans = ''
for i in s:
    ans += i
print(str(ans))