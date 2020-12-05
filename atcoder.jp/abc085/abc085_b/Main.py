N = int(input())
D = []
for i in range(N):
    d = int(input())
    D.append(d)
D = list(set(D))
D.sort()
print(len(D))