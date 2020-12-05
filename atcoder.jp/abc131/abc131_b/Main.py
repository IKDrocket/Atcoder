n,l = map(int,input().split())
s = list(range(1,n+1))
azi = []
ab = 100
for i in range(n):
    azi.append(l + i)
    if abs(ab) > abs(l + i):
        ab = l + i

print(sum(azi)-ab)