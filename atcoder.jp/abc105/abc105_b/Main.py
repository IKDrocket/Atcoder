n = int(input())

cMaxCnt = n//4
dMaxCnt = n//7

ans = 'No'
for cCnt in range(cMaxCnt+1):
    for dCnt in range(dMaxCnt+1):
        if n == 4*cCnt + 7*dCnt:
            ans = 'Yes'
            break
print(ans)  