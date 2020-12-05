n,k = map(int,input().split(' '))
l = set(range(1,n+1))
la = set()
for i in range(k):
    d = int(input())
    a = set(map(int,input().split()))
    la = la | a
print(len(l-la))