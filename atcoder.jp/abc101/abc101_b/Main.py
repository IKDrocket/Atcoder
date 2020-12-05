n = input()
l = [int(x) for x in list(str(n))]
S = sum(l)
if int(n) % S == 0:
    print("Yes")
else:
    print("No")