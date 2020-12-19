n = int(input())
ans = 0
for i in range(1,n+1):
    if str(i).count('7') or str(oct(i))[2:].count('7'):
        continue
    else:
        ans += 1
print(ans)