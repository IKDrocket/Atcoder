a,b,c,k = map(int,input().split())

ans = 0

if a <= k:
    ans += a
    k -= a
else:
    ans += k
    print(ans)
    exit()
if b <= k:
    k -= b
else:
    ans += k
    print(ans)
    exit()
if c <= k:
    ans -= c
    k -= c
else:
    ans -= k
    print(ans)
    exit()
print(ans)