n = int(input())
s = list(input())
Count = 0
for i in range(n):
    f = list(set(s[:(i+1)]))
    r = list(set(s[(i+1):]))
    count = 0
    for j in range(len(f)):
        for k in range(len(r)):
            if f[j] == r[k]:
                count += 1
    if Count < count:
        Count = count
print(Count)