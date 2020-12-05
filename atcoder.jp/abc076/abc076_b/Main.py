n=int(input())
k=int(input())
a=1
for i in range(n):
    if a*2>a+k:
       a=a+k
    else:
        a=a*2
print(a)