a = [list(map(int,input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

ans = 'No'
for i in range(3):
    if a[0][i] in b and a[1][i] in b and a[2][i] in b:
        ans = 'Yes'
    if a[i][0] in b and a[i][1] in b and a[i][2] in b:
        ans = 'Yes'
if (a[0][0] in b and a[1][1] in b and a[2][2] in b) \
    or (a[0][2] in b and a[1][1] in b and a[2][0]):
    ans = 'Yes'

print(ans)