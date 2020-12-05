a,b,k = map(int,input().split())
ans = []
if 2*k <= b-a+1:
    for i in range(k):
        ans.append(a+i)
        ans.append(b-i)
    ans = list(set(ans))
    ans = sorted(ans)
    for i in ans:
        print(i)
else:
    for i in range(a,b+1):
        print(i)
