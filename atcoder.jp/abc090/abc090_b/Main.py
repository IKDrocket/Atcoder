a,b = map(int,input().split())
ans = 0
for i in range(a,b+1):
    I = list(str(i))
    if I[0]==I[4] and I[1] == I[3]:
        ans+=1
print(ans)