S = list(input())
T = list(input())

cnt = 0
for s,t in zip(S,T):
    if s != t:
        cnt += 1 
    else:
        continue
print(cnt)