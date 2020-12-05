s = list(input())
S = ""
for i in range(len(s)):
    if s[i] == "B":
        if S == "":
            continue
        else:
            S = S[:-1]
    else:
        S += s[i]
print(S)