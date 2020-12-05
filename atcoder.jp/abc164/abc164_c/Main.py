n = int(input())
sdict = dict()
for _ in range(n):
    s = input()
    try:
        tryproc = sdict[s]
    except:
        sdict[s] = True
print(len(sdict))