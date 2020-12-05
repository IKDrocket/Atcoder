x = list(map(int,input().split()))
x.sort()
ans=0
while not x[0]==x[1]==x[2]:
    if x[0]%2 != x[1]%2:
        x[1]+=1
        x[2]+=1
        ans+=1
    elif x[1]!=x[2]:
        x[0]+=1
        x[1]+=1
        ans+=1 
    else:
        x[0]+=2
        ans+=1
print(ans)
