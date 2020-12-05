k, n = map(int,input().split())

a = list(map(int,input().split()))
a.append(k+a[0])
maxgap = 0
al = a[-1] - a[0]

for l in range(n):
    gap = a[l+1] - a[l]
    maxgap = max(maxgap,gap)
print(al - maxgap)