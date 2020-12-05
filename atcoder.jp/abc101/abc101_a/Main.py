n = input()
ans = 0
for i in n:
    if i == "+":
        ans += 1
    else:
        ans -= 1
print(ans)