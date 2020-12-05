n = int(input())
t,x,y = (0,0,0)
Flag = True
for i in range(n):
    nt,nx,ny = list(map(int,input().split()))
    dist = abs(nx-x) + abs(ny-y)
    if dist > nt-t or (nt+nx+ny)%2 != 0:
        Flag = False
if Flag == True:
    print("Yes")
else:
    print("No")