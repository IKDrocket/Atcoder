n,m = map(int,input().split())
a = list(map(int,input().split()))

cnt = 0
for a_ in a:
    if a_ < sum(a)/(4*m):
        cnt += 1
if m > n - cnt:
    print('No')
else:
    print('Yes')