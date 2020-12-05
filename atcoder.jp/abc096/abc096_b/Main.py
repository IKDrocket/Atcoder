x = list(map(int,input().split()))
x = sorted(x)
k = int(input())
for i in range(k):
    x[2] *= 2
print(sum(x))