h,w = map(int,input().split())
s = [input() for i in range(h)]
ans = "Yes"
for i in range(h-1):
    for j in range(w-1):
        if s[i][j] == "#" and s[i][j] != s[i][j+1] and s[i][j] != s[i+1][j]:
            if (j >= 1 and s[i][j] == "#" and s[i][j] == s[i][j-1]) or (i >= 1 and s[i][j] == "#" and s[i][j] == s[i-1][j]):
                continue
            else:
                ans = "No"
                print(ans)
                exit()
        else:
            continue
print(ans)

            
        