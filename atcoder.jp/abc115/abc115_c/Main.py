n,k = map(int,input().split())
h = sorted([int(input()) for i in range(n)])
d = [h[i+k-1]-h[i] for i in range(n-k+1)]
print(min(d))