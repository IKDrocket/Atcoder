a,b = map(int,input().split())
c = [1]
n = 1
for i in range(2,1000):
    c.append(n + i)
    n += i
print(c[b-a-2]-a)