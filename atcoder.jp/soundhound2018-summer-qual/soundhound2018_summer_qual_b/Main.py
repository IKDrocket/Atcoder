s = input()
S = list(s)
w = int(input())


ans = ""

for i in range(1,len(s)):
    if i  == 1:
        ans += S[0]
    if i % w == 0:
        ans += S[i]

print(ans)