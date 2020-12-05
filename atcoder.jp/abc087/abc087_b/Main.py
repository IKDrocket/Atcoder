a = int(input())
b = int(input())
c = int(input())

x = int(input())

ans = 0
for cnt500 in range(a+1):
    for cnt100 in range(b+1):
            if 0 <= x - (500*cnt500 + 100*cnt100) <= 50*c:
                ans += 1
print(ans)