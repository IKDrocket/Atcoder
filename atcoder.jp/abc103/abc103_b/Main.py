s = list(input())
t = list(input())
ans = "No"
for i in range(len(s)):
    if s == t:
        ans = "Yes"
    else:
        s = list(s[-1]) + s[:-1]

print(ans)