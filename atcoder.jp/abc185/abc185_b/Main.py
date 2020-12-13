n,m,t = map(int,input().split())

b_ = n
t_ = 0
for _ in range(m):
    a, b = map(int,input().split())
    b_ -= a-t_
    if b_ <= 0:
        print('No')
        exit()
    b_ += (b-a)
    b_ = min(n, b_)
    t_ = b
b_ -= (t-t_)


if b_ <= 0:
    print('No')
else:
    print('Yes')