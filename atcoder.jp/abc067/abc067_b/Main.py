N,K = map(int,input().split())
l = map(int,input().split())
l = list(l)
l.sort(reverse=True)
l_ = l[:K]
print(sum(l_))