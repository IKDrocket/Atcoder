n = int(input())
s = list(input())
left_w = 0
right_e = s[1:].count("E")
ans = right_e
for i in range(1,n):
    if s[i-1] == "W":
        left_w += 1
    if s[i] == "E":
        right_e -= 1
    ans = min(ans,right_e +left_w)
print(ans)
    