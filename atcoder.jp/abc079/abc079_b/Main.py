N = int(input())
L = 2
l = 1

for i in range(N-1):
    if i%2==0:
        L = L+l
    else:
        l = l+L
if N%2==0:
    print(L)
else:
    print(l)