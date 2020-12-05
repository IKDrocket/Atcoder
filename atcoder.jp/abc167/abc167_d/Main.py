n,k = map(int,input().split())

a = [0]
a.extend(list(map(int,input().split())))
l = [None]*(n+1)

now = 1
step = 0
l[now] = 0
while k:
    now = a[now]
    step += 1
    k -= 1
    if l[now] is not None:
        looplen = (step - l[now])
        k = k%looplen
    else:
        l[now] = step
print(now)