n = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
sc = []
for i in range(n):
    sc.append(sum(A1[:i+1]+A2[i:]))
print(max(sc))