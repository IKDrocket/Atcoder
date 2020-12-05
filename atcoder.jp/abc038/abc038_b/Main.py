h,w = map(int,input().split())
H,W = map(int,input().split())
if h == H:
    print("YES")
elif h == W:
    print("YES")
elif H == w:
    print("YES")
elif W == w:
    print("YES")
else:
    print("NO")
