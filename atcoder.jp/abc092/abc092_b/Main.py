n = int(input())
d,x = map(int,input().split())
sum = 0
for i in range(n):
    a = int(input())
    if a == 1:
        sum += d
    else:
        sum += (1+(d-1)//a)
print(sum+x)