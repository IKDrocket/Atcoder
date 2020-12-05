import numpy as np
n, d = map(int,input().split())
pArray = [np.array(list(map(int, input().split()))) for i in range(n)]

cnt = 0
for i in range(len(pArray)-1):
    for j in range(i+1,len(pArray)):
        dist = np.sqrt(sum((pArray[i] - pArray[j])**2))
        if dist.is_integer():
            cnt += 1
print(cnt)