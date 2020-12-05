n = int(input())
diff = 0
a = [int(x) for x in input().split()]
for i in range(n):
    for j in range(i+1,n):
        d = abs(a[i]-a[j])
        if d > diff:
            diff = d
print(diff)