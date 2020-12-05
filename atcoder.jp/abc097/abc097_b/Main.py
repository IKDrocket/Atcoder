x = int(input())
ans = 1
for i in range(2,1000):
    for j in range(2,1000):
        if i**j <= x:
            ans = max(ans,i**j)
        else:
            break
print(ans)