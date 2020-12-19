import numpy as np
n, w = map(int,input().split())

l = []
for _ in range(n):
    a = list(map(int,input().split()))
    l.extend(a)
ans = sum(np.array(l) - min(l))
print(ans)