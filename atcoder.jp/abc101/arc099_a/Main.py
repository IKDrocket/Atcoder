N,K = map(int,input().split())
A = list(input())
Ans = 0
 
if (N-1)%(K-1)==0:
    Ans = (N-1)//(K-1)
else:
    Ans = (N-1)//(K-1) + 1
 
print(Ans)