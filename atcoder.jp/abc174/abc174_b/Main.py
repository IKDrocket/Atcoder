n, d = map(int,input().split())
cnt = 0
for i in range(n):
    x, y = map(int,input().split())
    cnt += 1 if d**2 >= x**2 + y**2 else 0
print(cnt)