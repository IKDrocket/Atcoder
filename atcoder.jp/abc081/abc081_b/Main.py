n=int(input())
a=list(map(int,input().split()))
num=0
while True:
    sum=0
    for i in range(n):
        if a[i]%2==0:
            sum+=1
    if sum==n:
        num+=1
        for i in range(n):
            a[i]/=2
    else:
        break
print(num)
