n,m,X,Y = map(int,input().split())
ans = "War"
if X < Y:
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    if max(x) < min(y) and X < min(y) <= Y :
        ans = "No War"
print(ans)