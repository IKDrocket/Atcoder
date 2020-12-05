n = int(input())
x = list(map(int,input().split()))
x_sorted = sorted(x)
mid = n//2
m1 = x_sorted[mid-1]
m2 = x_sorted[mid]
for i in range(n):
    if x[i] <= m1:
        print(m2)
    else:
        print(m1)

