n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        x1 = array[i][0]
        y1 = array[i][1]
        x2 = array[j][0]
        y2 = array[j][1]
        a = abs(y2 - y1) / abs(x2 - x1)
        if a <= 1:
            ans += 1
print(ans)