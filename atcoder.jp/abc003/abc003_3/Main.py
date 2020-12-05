N,K =map(int,input().split())
r = list(map(int, input().split()))
r.sort()
R = 0
for i in range(K):
   R = (R + r[N-K+i])/2
print(R)
    
