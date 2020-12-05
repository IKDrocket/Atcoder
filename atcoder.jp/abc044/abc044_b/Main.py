alp = "abcdefghijklmnopqrstyvwxyz"
alp = (list(alp))
w = list(input())
flag = 0
for i in range(26):
    if w.count(alp[i]) % 2 == 0:
        continue
    else:
        flag = 1
        break
if flag == 0:
    print("Yes")
else:
    print("No")