S = input()
T = input()
n = len(S)
At = ["a","t","c","o","d","e","r"]

for i in range(n):
    if S[i] != T[i]:
        if S[i] == "@" and T[i] in At:
            continue
        elif T[i] == "@" and S[i] in At:
            continue
        else:
            print("You will lose")
            break
else:
    print("You can win")
 