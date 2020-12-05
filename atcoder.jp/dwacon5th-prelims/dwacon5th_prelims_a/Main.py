import numpy as np

n = int(input())
a = list(map(int,input().split()))
median = np.average(a)
idx = np.abs(np.asarray(a) - median).argmin()

ans = 0
for i in range(n):
    if a[i] == a[idx]:
        ans = i
        break
print(ans)